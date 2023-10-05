from finstmt.forecast.config import ForecastItemConfig
from finstmt.items.config import ItemConfig

# Balance Sheet config template
#TODO: Use a registration Mechanism to make a special config file, it can using a dictionary with the field name as key and corrsponding name as value.
# Would be better to use regex instead of names list. Need to first add that infrastructure,
# then apply it to the Balance Sheet config.

# Note that each possible extract_name must be unique, it cannot be included in multiple lists
# Also note that all incoming names will be converted to lower case and stripped of punctuation,
# then split on _ and joined with space before matching these names
BALANCE_SHEET_INPUT_ITEMS = [
    ItemConfig(
        "cash",
        "Cash and Cash Equivalents",
        extract_names=[
        ],
        forecast_config=ForecastItemConfig(plug=True),
    ),
    ItemConfig(
        "st_invest",
        "Short-Term Investments",
        extract_names=[
        ],
    ),
    ItemConfig(
        "cash_and_st_invest",
        "Cash and Short-Term Investments",
        extract_names=[
        ],
        expr_str="cash[t] + st_invest[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "receivables",
        "Receivables",
        extract_names=[

        ],
        forecast_config=ForecastItemConfig(pct_of="revenue"),
    ),
    ItemConfig(
        "inventory",
        "Inventory",
        extract_names=[

        ],
        forecast_config=ForecastItemConfig(pct_of="revenue"),
    ),
    ItemConfig(
        "def_tax_st",
        "Deferred Tax Assets, Current",
        extract_names=[
           
        ],
    ),
    ItemConfig(
        "other_current_assets",
        "Other Current Assets",
        extract_names=[
        ],
    ),
    ItemConfig(
        "total_current_assets",
        "Total Current Assets",
        extract_names=[
        ],
        expr_str="cash_and_st_invest[t] + receivables[t] + inventory[t] + def_tax_st[t] + other_current_assets[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "gross_ppe",
        "Gross Property, Plant & Equipment",
        extract_names=[
        ],
    ),
    ItemConfig(
        "dep",
        "Accumulated Depreciation",
        extract_names=[
        ],
    ),
    ItemConfig(
        "net_ppe",
        "Net Property, Plant & Equipment",
        extract_names=[
        ],
        expr_str="gross_ppe[t] - dep[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "goodwill",
        "Goodwill and Intangible Assets",
        extract_names=[
        ]
        # TODO [#50]: need to be able to extract from multiple items at once
        #
        # Morningstar financial statements have Goodwill and then Intangibles other than Goodwill,
        # both of those should be coming into the Goodwill and Intagible Assets variable.
    ),
    ItemConfig(
        "lt_invest",
        "Long-Term Investments",
        extract_names=[
        ],
    ),
    ItemConfig(
        "def_tax_lt",
        "Deferred Tax Assets, Long-Term",
        extract_names=[
        ],
    ),
    ItemConfig(
        "other_lt_assets",
        "Other Long-Term Assets",
        extract_names=[
        ],
    ),
    ItemConfig(
        "total_non_current_assets",
        "Total Non-Current Assets",
        extract_names=[
        ],
        expr_str="net_ppe[t] + goodwill[t] + lt_invest[t] + def_tax_lt[t] + other_lt_assets[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "total_assets",
        "Total Assets",
        extract_names=[
            ],
        expr_str="total_current_assets[t] + total_non_current_assets[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
            balance_with="total_liab_and_equity",
        ),
    ),
    ItemConfig(
        "payables",
        "Payables",
        extract_names=[
        ],
        forecast_config=ForecastItemConfig(pct_of="revenue"),
    ),
    ItemConfig(
        "st_debt",
        "Short-Term Debt",
        extract_names=[
        ],
        forecast_config=ForecastItemConfig(pct_of="total_debt"),
    ),
    ItemConfig(
        "current_lt_debt",
        "Current Portion of Long-Term Debt",
        extract_names=[
        ],
        forecast_config=ForecastItemConfig(pct_of="total_debt"),
    ),
    ItemConfig(
        "tax_liab_st",
        "Tax Liabilities, Short-Term",
        extract_names=[
        ],
    ),
    ItemConfig(
        "other_current_liab",
        "Other Current Liabilities",
        extract_names=[
        ],
    ),
    ItemConfig(
        "total_current_liab",
        "Total Current Liabilities",
        extract_names=[
        ],
        expr_str="payables[t] + st_debt[t] + tax_liab_st[t] + current_lt_debt[t] + other_current_liab[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "lt_debt",
        "Long-Term Debt",
        extract_names=[
        ],
        forecast_config=ForecastItemConfig(plug=True),
    ),
    ItemConfig(
        "total_debt",
        "Total Debt",
        extract_names=["total debt"],
        expr_str="st_debt[t] + lt_debt[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "deferred_rev",
        "Deferred Revenue",
        extract_names=[
        ],
    ),
    ItemConfig(
        "tax_liab_lt",
        "Tax Liabilities, Long-Term",
        extract_names=[
        ],
    ),
    ItemConfig(
        "deposit_liab",
        "Deposit Liabilities",
        extract_names=[
        ],
    ),
    ItemConfig(
        "other_lt_liab",
        "Other Long-Term Liabilities",
        extract_names=[
        ],
    ),
    ItemConfig(
        "total_non_current_liab",
        "Total Non-Current Liabilities",
        extract_names=[
        ],
        expr_str="lt_debt[t] + deferred_rev[t] + tax_liab_lt[t] + deposit_liab[t] + other_lt_liab[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "total_liab",
        "Total Liabilities",
        extract_names=[
        ],
        expr_str="total_non_current_liab[t] + total_current_liab[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "common_stock",
        "Common Stock",
        extract_names=[
        ],
    ),
    ItemConfig(
        "other_income",
        "Other Comprehensive Income",
        extract_names=[
        ],
        force_positive=False,
    ),
    ItemConfig(
        "retained_earnings",
        "Retained Earnings",
        extract_names=[
        ],
        force_positive=False,
        # TODO [#4]: forecast of retained earnings should be calculated
        #
        # Should be a calculation of retained_earnings[t-1] + net income[t] - dividends[t]
    ),
    ItemConfig(
        "minority_interest",
        "Minority Interest",
        extract_names=[
        ],
    ),
    ItemConfig(
        "total_equity",
        "Total Stockholder's Equity",
        extract_names=[
        ],
        expr_str="other_income[t] + retained_earnings[t] + common_stock[t] + minority_interest[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
    ),
    ItemConfig(
        "total_liab_and_equity",
        "Total Liabilities and Equity",
        extract_names=[
        ],
        expr_str="total_liab[t] + total_equity[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
            balance_with="total_assets",
        ),
    ),
    ItemConfig(
        "nwc",
        "Net Working Capital",
        extract_names=[
        ],
        expr_str="receivables[t] + inventory[t] - payables[t]",
        forecast_config=ForecastItemConfig(
            make_forecast=False,
        ),
        display_verbosity=2,
    ),
]
