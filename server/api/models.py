from django.db import models


# Create your models here.

class Base(models.Model):
    is_show = models.BooleanField(default=1)
    is_delete = models.BooleanField(default=1)
    create = models.TimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Food(Base):  # 商品
    name = models.CharField(max_length=255, verbose_name="菜品名")
    price = models.CharField(max_length=255, verbose_name="原单价")
    img = models.ImageField(upload_to="static/img", verbose_name="展示图")
    detail = models.OneToOneField(to="FoodDetail", related_name="food_detail", on_delete=models.DO_NOTHING,
                                  db_constraint=False, verbose_name="菜品详情")
    category = models.ForeignKey(to="Category", related_name="category", on_delete=models.DO_NOTHING,
                                 verbose_name="菜品分类")

    # @property
    # def FoodDetails(self):
    #     from api.ser.store_ser import FoodDetailModelSerializer
    #     print(self.detail_id)
    #     detail_obj = FoodDetail.objects.filter(pk=self.detail_id).first()
    #     return FoodDetailModelSerializer(instance=detail_obj).data

    def __str__(self):
        return self.name


class FoodDetail(Base):  # 商品详情
    sale_num = models.CharField(max_length=255, verbose_name="销售量")
    ingredient = models.CharField(max_length=255, verbose_name="配料")
    dec = models.CharField(max_length=255, verbose_name="菜品描述")

    def __str__(self):
        return "菜品详情"


class Category(Base):  # 分类
    name = models.CharField(max_length=255, verbose_name="目录名")
    @property
    def foods(self):
        from api.ser.store_ser import FoodsModelSerializer
        return FoodsModelSerializer(instance=self.category.all(), many=True).data

    def __str__(self):
        return self.name


class Warehouse(Base):  # 仓库
    num = models.CharField(max_length=255, verbose_name="库存量")
    food = models.OneToOneField(to="Food", related_name="food", on_delete=models.DO_NOTHING, verbose_name="菜品")

    def __str__(self):
        return self.food.name


##################################################################

class BigOrder(Base):  # 总订单
    choice = ((0, '未支付'), (1, '已支付'), (2, '以接单'), (3, '订单完成'))
    open_id = models.CharField(max_length=255, verbose_name="微信用户ID")
    order_id = models.CharField(max_length=255, verbose_name="订单号")
    status = models.CharField(choices=choice, max_length=255, default=0, verbose_name='订单状态')
    address = models.CharField(max_length=255, verbose_name="收货地址")


class SmallOrder(Base):  # 子订单
    big_order = models.ForeignKey(to="BigOrder", related_name="big_order", on_delete=models.DO_NOTHING,
                                  db_constraint=True, verbose_name="大订单")
    food_id = models.CharField(max_length=255, verbose_name="商品ID")
    is_discount = models.BooleanField(default=0, verbose_name="折扣")


class Active(Base):  # 活动
    name = models.CharField(max_length=255, verbose_name="活动名称")
    food = models.OneToOneField(to="Food", related_name="food_active", on_delete=models.DO_NOTHING, verbose_name="菜品")
    detail = models.CharField(max_length=255, verbose_name="活动内容")
    discount = models.CharField(max_length=255, verbose_name="折扣")


######################################################################
class Address(Base):  # 收货地址
    # id 1 2 3
    open_id = models.CharField(max_length=255)
    add = models.CharField(max_length=255, verbose_name="收货地址")
    phone = models.CharField(max_length=255, verbose_name="收货电话")
    rec_name = models.CharField(max_length=255, verbose_name="收货人姓名")
