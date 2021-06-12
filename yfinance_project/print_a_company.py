import yfinance as yf


writing_list = []
company = input('input company: ')
print()

# get stock info
company_info= yf.Ticker(company)
# print(company_info.info)

# get historical market data
hist = company_info.history(period='max')
writing_list.append('<<<historical market dat>>>\n')
writing_list.append(str(hist))
writing_list.append('')
print(hist)

# show actions (dividends, splits)
actions = str(company_info.actions)
writing_list.append('<<<actions>>>\n')
writing_list.append(str(actions))
writing_list.append('')
print(actions)

# show dividends
dividends = company_info.dividends
writing_list.append('<<<dividends>>>\n')
writing_list.append(str(dividends))
writing_list.append('')
print(dividends)

# show splits
splits = company_info.splits
writing_list.append('<<<splits>>>\n')
writing_list.append(str(splits))
writing_list.append('')
print(splits)

# show financials
financials = company_info.financials
quarterly_financials = company_info.quarterly_financials
writing_list.append('<<<financials>>>\n')
writing_list.append(str(financials))
writing_list.append(str(quarterly_financials))
writing_list.append('')
print(financials)
print(quarterly_financials)

# show major holders
major_holders = company_info.major_holders
writing_list.append('<<<major holders>>>\n')
writing_list.append(str(major_holders))
writing_list.append('')
print(major_holders)

# show institutional holders
institutional_holders = company_info.institutional_holders
writing_list.append('<<<institutional holders>>>\n')
writing_list.append(str(institutional_holders))
writing_list.append('')
print(institutional_holders)

# show balance sheet
balance_sheet = company_info.balance_sheet
quarterly_balance_sheet = company_info.quarterly_balance_sheet
writing_list.append('<<<balance sheet>>>\n')
writing_list.append(str(balance_sheet))
writing_list.append(str(quarterly_balance_sheet))
writing_list.append('')
print(balance_sheet)
print(quarterly_balance_sheet)

# cashflow
cashflow = company_info.cashflow
quarterly_cashflow = company_info.quarterly_cashflow
writing_list.append('<<<cashflow>>>\n')
writing_list.append(str(cashflow))
writing_list.append(str(quarterly_cashflow))
writing_list.append('')
print(cashflow)
print(quarterly_cashflow)

# show earnings
earnings = company_info.earnings
quarterly_earnings = company_info.quarterly_earnings
writing_list.append('<<<earnings>>>\n')
writing_list.append(str(earnings))
writing_list.append(str(quarterly_earnings))
writing_list.append('')
print(earnings)
print(quarterly_earnings)

# show sustainability
sustainability = company_info.sustainability
writing_list.append('<<<sustainability>>>\n')
writing_list.append(str(sustainability))
writing_list.append('')
print(sustainability)

# show analysts recommendations
recommendations = company_info.recommendations
writing_list.append('<<<analysts>>>\n')
writing_list.append(str(recommendations))
writing_list.append('')

# show next event (earnings, etc)
calendar = company_info.calendar
writing_list.append('<<<next event>>>\n')
writing_list.append(str(calendar))
writing_list.append('')

# show ISIN code - *experimental*
# ISIN = International Securities Identifications Number
isin = company_info.isin
writing_list.append('<<<ISIN>>>\n')
writing_list.append(str(isin))
writing_list.append('')

# show options expirations
options = company_info.options
writing_list.append('<<<options>>>\n')
writing_list.append(str(options))
writing_list.append('')
print(options)

# get option chain for specific experation
wanna_date = '2021-06-11'
opt = company_info.option_chain(wanna_date)
writing_list.append(f'<<<{wanna_date}\'calls & puts>>>\n')
writing_list.append('<calls>')
writing_list.append(str(opt.calls))
writing_list.append('<puts>')
writing_list.append(str(opt.puts))
print(opt.calls)
print(opt.puts)

with open(company+'.txt', 'w') as txt:
    for i in writing_list:
        txt.write(i+'\n')

print(f'{company}의 주가 정보가 {company}.txt에 저장되었습니다.')

