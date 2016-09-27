from __future__ import unicode_literals
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    extra_information = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return self.name

class Destination(models.Model):
    port_of_loading = models.CharField(max_length=200, blank=True, null=True)
    loading_location_type = models.CharField(max_length=200, blank=True, null=True)
    port_of_discharge = models.CharField(max_length=200, blank=True, null=True)
    discharge_location_type = models.CharField(max_length=200, blank=True, null=True)

class FinalDeliveryDestination(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    contact_person_extra = models.TextField(max_length=200, blank=True, null=True)

class AIFCargoSales(models.Model):
    quantity = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    net_weight = models.CharField(max_length=200, blank=True, null=True)
    pieces = models.CharField(max_length=200, blank=True, null=True)
    packing = models.CharField(max_length=200, blank=True, null=True)
    dimensions = models.CharField(max_length=200, blank=True, null=True)

class FCLCargoSales(models.Model):
    container_type = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    net_weight = models.CharField(max_length=200, blank=True, null=True)

class LCLCargoSales(models.Model):
    quantity = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    net_weight = models.CharField(max_length=200, blank=True, null=True)
    pieces = models.CharField(max_length=200, blank=True, null=True)
    packing = models.CharField(max_length=200, blank=True, null=True)

class ShippingLine(models.Model):
    prefered = models.CharField(max_length=200, blank=True, null=True)
    any = models.CharField(max_length=200, blank=True, null=True)

class IMOClass(models.Model):
    hazardous = models.CharField(max_length=200, blank=True, null=True)
    non_hazardous = models.CharField(max_length=200, blank=True, null=True)

class ShipmentTerm(models.Model):
    ex_work = models.CharField(max_length=200, blank=True, null=True)
    fas = models.CharField(max_length=200, blank=True, null=True)
    fob = models.CharField(max_length=200, blank=True, null=True)
    cf = models.CharField(max_length=200, blank=True, null=True)
    cif = models.CharField(max_length=200, blank=True, null=True)
    others = models.TextField(blank=True, null=True)

class RateRequest(models.Model):
    TYPE_CHOICES = (
        ('AIF', 'AIF'),
        ('FCL', 'FCL'),
        ('LCL', 'LCL')
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    sales_person = models.ForeignKey('authentication.User', related_name='rate_requests', blank=True, null=True)
    client = models.ForeignKey('main.Client', related_name='rate_requests', blank=True, null=True)
    destination = models.OneToOneField('main.Destination', related_name='rate_request', blank=True, null=True)
    final_delivery_destination = models.OneToOneField('main.FinalDeliveryDestination', related_name='rate_request', blank=True, null=True)
    required_delivery_time_within = models.CharField(max_length=200, blank=True, null=True)
    aif_cargo_details = models.OneToOneField('main.AIFCargoSales', related_name='rate_request', blank=True, null=True)
    fcl_cargo_details = models.OneToOneField('main.FCLCargoSales', related_name='rate_request', blank=True, null=True)
    lcl_cargo_details = models.OneToOneField('main.LCLCargoSales', related_name='rate_request', blank=True, null=True)
    shipping_line = models.OneToOneField('main.ShippingLine', related_name='rate_request', null=True, blank=True)
    imo_class = models.OneToOneField('main.IMOClass', related_name='rate_request', blank=True, null=True)
    shipment_term = models.OneToOneField('main.ShipmentTerm', related_name='rate_request', blank=True, null=True)
    payment_term = models.CharField(max_length=200, blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Rate Request'
        verbose_name_plural = 'Rate Requests'
    def __str__(self):
        return self.client.name

class AIFCargoOperations(models.Model):
    commodity = models.CharField(max_length=200, blank=True, null=True)
    num_of_packages = models.CharField(max_length=200, blank=True, null=True)
    actual_weight = models.CharField(max_length=200, blank=True, null=True)
    chargeable_weight = models.CharField(max_length=200, blank=True, null=True)
    dimensions = models.CharField(max_length=200, blank=True, null=True)
    air_line = models.CharField(max_length=200, blank=True, null=True)
    transit_time = models.CharField(max_length=200, blank=True, null=True)
    route = models.CharField(max_length=200, blank=True, null=True)
    departure_date = models.CharField(max_length=200, blank=True, null=True)
    arrival_date = models.CharField(max_length=200, blank=True, null=True)
    mawb_number = models.CharField(max_length=200, blank=True, null=True)
    hawb_number = models.CharField(max_length=200, blank=True, null=True)

class FCLCargoOperations(models.Model):
    shipping_line = models.CharField(max_length=200, blank=True, null=True)
    container_type = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    net_weight = models.CharField(max_length=200, blank=True, null=True)

class LCLCargoOperations(models.Model):
    shipping_line = models.CharField(max_length=200, blank=True, null=True)
    container_type = models.CharField(max_length=200, blank=True, null=True)
    num_of_packages = models.CharField(max_length=200, blank=True, null=True)
    commodity = models.CharField(max_length=200, blank=True, null=True)
    gross_weight = models.CharField(max_length=200, blank=True, null=True)
    net_weight = models.CharField(max_length=200, blank=True, null=True)
    dimensions_cbm = models.CharField(max_length=200, blank=True, null=True)

class AIFQuotation(models.Model):
    air_freight_kg_net = models.CharField(max_length=200, blank=True, null=True)
    air_freight_kg_selling = models.CharField(max_length=200, blank=True, null=True)
    fuel_sur_charge_kg_net = models.CharField(max_length=200, blank=True, null=True)
    fuel_sur_charge_kg_selling = models.CharField(max_length=200, blank=True, null=True)
    security_fees_kg_net = models.CharField(max_length=200, blank=True, null=True)
    security_fees_kg_selling = models.CharField(max_length=200, blank=True, null=True)
    exw_charges_net = models.CharField(max_length=200, blank=True, null=True)
    exw_charges_selling = models.CharField(max_length=200, blank=True, null=True)
    screening_fees_net = models.CharField(max_length=200, blank=True, null=True)
    screening_fees_selling = models.CharField(max_length=200, blank=True, null=True)
    storage_net = models.CharField(max_length=200, blank=True, null=True)
    storage_selling = models.CharField(max_length=200, blank=True, null=True)
    inland_net = models.CharField(max_length=200, blank=True, null=True)
    inland_selling = models.CharField(max_length=200, blank=True, null=True)
    packing_net = models.CharField(max_length=200, blank=True, null=True)
    packing_selling = models.CharField(max_length=200, blank=True, null=True)
    taxes_duties_net = models.CharField(max_length=200, blank=True, null=True)
    taxes_duties_selling = models.CharField(max_length=200, blank=True, null=True)
    handling_fees_net = models.CharField(max_length=200, blank=True, null=True)
    handling_fees_selling = models.CharField(max_length=200, blank=True, null=True)
    p_share_net = models.CharField(max_length=200, blank=True, null=True)
    p_share_selling = models.CharField(max_length=200, blank=True, null=True)

class FCLQuotation(models.Model):
    ocean_freight_net = models.CharField(max_length=200, blank=True, null=True)
    ocean_freight_selling = models.CharField(max_length=200, blank=True, null=True)
    thc_net = models.CharField(max_length=200, blank=True, null=True)
    thc_selling = models.CharField(max_length=200, blank=True, null=True)
    transporation_net = models.CharField(max_length=200, blank=True, null=True)
    transporation_selling = models.CharField(max_length=200, blank=True, null=True)
    transfer_net = models.CharField(max_length=200, blank=True, null=True)
    transfer_selling = models.CharField(max_length=200, blank=True, null=True)
    clearance_pol_net = models.CharField(max_length=200, blank=True, null=True)
    clearance_pol_selling = models.CharField(max_length=200, blank=True, null=True)
    clearance_pod_net = models.CharField(max_length=200, blank=True, null=True)
    clearance_pod_selling = models.CharField(max_length=200, blank=True, null=True)
    bl_fees_net = models.CharField(max_length=200, blank=True, null=True)
    bl_fees_selling = models.CharField(max_length=200, blank=True, null=True)
    telex_release_net = models.CharField(max_length=200, blank=True, null=True)
    telex_release_selling = models.CharField(max_length=200, blank=True, null=True)
    ex_work_net = models.CharField(max_length=200, blank=True, null=True)
    ex_work_selling = models.CharField(max_length=200, blank=True, null=True)
    official_receipts_net = models.CharField(max_length=200, blank=True, null=True)
    official_receipts_selling = models.CharField(max_length=200, blank=True, null=True)

class LCLQuotation(models.Model):
    ocean_freight_net = models.CharField(max_length=200, blank=True, null=True)
    ocean_freight_selling = models.CharField(max_length=200, blank=True, null=True)
    thc_net = models.CharField(max_length=200, blank=True, null=True)
    thc_selling = models.CharField(max_length=200, blank=True, null=True)
    transporation_net = models.CharField(max_length=200, blank=True, null=True)
    transporation_selling = models.CharField(max_length=200, blank=True, null=True)
    transfer_net = models.CharField(max_length=200, blank=True, null=True)
    transfer_selling = models.CharField(max_length=200, blank=True, null=True)
    clearance_pol_net = models.CharField(max_length=200, blank=True, null=True)
    clearance_pol_selling = models.CharField(max_length=200, blank=True, null=True)
    clearance_pod_net = models.CharField(max_length=200, blank=True, null=True)
    clearance_pod_selling = models.CharField(max_length=200, blank=True, null=True)
    bl_fees_net = models.CharField(max_length=200, blank=True, null=True)
    bl_fees_selling = models.CharField(max_length=200, blank=True, null=True)
    telex_release_net = models.CharField(max_length=200, blank=True, null=True)
    telex_release_selling = models.CharField(max_length=200, blank=True, null=True)
    ex_work_net = models.CharField(max_length=200, blank=True, null=True)
    ex_work_selling = models.CharField(max_length=200, blank=True, null=True)
    official_receipts_net = models.CharField(max_length=200, blank=True, null=True)
    official_receipts_selling = models.CharField(max_length=200, blank=True, null=True)

class ExtraNotes(models.Model):
    free_time_at_destination = models.CharField(max_length=200, blank=True, null=True)
    vessel_available = models.CharField(max_length=200, blank=True, null=True)
    route = models.CharField(max_length=200, blank=True, null=True)
    transit_time = models.CharField(max_length=200, blank=True, null=True)
    offer_validity = models.CharField(max_length=200, blank=True, null=True)

class Quotation(models.Model):
    TYPE_CHOICES = (
        ('AIF', 'AIF'),
        ('FCL', 'FCL'),
        ('LCL', 'LCL')
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    operations_person = models.ForeignKey('authentication.User', related_name='quotations', blank=True, null=True)
    client = models.ForeignKey('main.Client', related_name='quotations', blank=True, null=True)
    agent_details = models.CharField(max_length=200, blank=True, null=True)
    co_loader = models.CharField(max_length=200, blank=True, null=True)
    destination = models.OneToOneField('main.Destination', related_name='quotation', blank=True, null=True)
    aif_cargo_details = models.OneToOneField('main.AIFCargoOperations', related_name='quotation', blank=True, null=True)
    fcl_cargo_details = models.OneToOneField('main.FCLCargoOperations', related_name='quotation', blank=True, null=True)
    lcl_cargo_details = models.OneToOneField('main.LCLCargoOperations', related_name='quotation', blank=True, null=True)
    aif_quotation = models.OneToOneField('main.AIFQuotation', related_name='quotation', blank=True, null=True)
    fcl_quotation = models.OneToOneField('main.FCLQuotation', related_name='quotation', blank=True, null=True)
    lcl_quotation = models.OneToOneField('main.LCLQuotation', related_name='quotation', blank=True, null=True)
    extra_notes = models.OneToOneField('main.ExtraNotes', related_name='quotation', blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Quotation'
        verbose_name_plural = 'Quotations'
    def __str__(self):
        return self.client.name