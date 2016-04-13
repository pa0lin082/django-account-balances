# -*- coding: utf-8 -*-
__author__ = 'elfo'

# import the logging library
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.conf.urls import patterns, url
from accounts.dashboard import views
from django.contrib.admin.views.decorators import staff_member_required



account_list_view = staff_member_required(views.AccountListView.as_view())
account_create_view = staff_member_required(views.AccountCreateView.as_view())
account_update_view = staff_member_required(views.AccountUpdateView.as_view())
account_transactions_view = staff_member_required(views.AccountTransactionsView.as_view())
account_freeze_view = staff_member_required(views.AccountFreezeView.as_view())
account_thaw_view = staff_member_required(views.AccountThawView.as_view())
account_top_up_view = staff_member_required(views.AccountTopUpView.as_view())

transfer_list_view = staff_member_required(views.TransferListView.as_view())
transfer_detail_view = staff_member_required(views.TransferDetailView.as_view())

report_deferred_income = staff_member_required(views.DeferredIncomeReportView.as_view())
report_profit_loss = staff_member_required(views.ProfitLossReportView.as_view())


urlpatterns = patterns('',
            url(r'^$',
                account_list_view,
                name='accounts-list'),
            url(r'^create/$', account_create_view,
                name='accounts-create'),
            url(r'^(?P<pk>\d+)/update/$', account_update_view,
                name='accounts-update'),
            url(r'^(?P<pk>\d+)/$', account_transactions_view,
                name='accounts-detail'),
            url(r'^(?P<pk>\d+)/freeze/$', account_freeze_view,
                name='accounts-freeze'),
            url(r'^(?P<pk>\d+)/thaw/$', account_thaw_view,
                name='accounts-thaw'),
            url(r'^(?P<pk>\d+)/top-up/$', account_top_up_view,
                name='accounts-top-up'),
            url(r'^transfers/$', transfer_list_view,
                name='transfers-list'),
            url(r'^transfers/(?P<reference>[A-Z0-9]{32})/$',
                transfer_detail_view,
                name='transfers-detail'),
            url(r'^reports/deferred-income/$',
                report_deferred_income,
                name='report-deferred-income'),
            url(r'^reports/profit-loss/$',
                report_profit_loss,
                name='report-profit-loss'),
        )