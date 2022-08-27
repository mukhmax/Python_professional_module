from application.salary import calculate_salary
from application.db.people import get_employees
from tradingview_ta import TA_Handler, Interval

if __name__ == '__main__':
    calculate_salary()
    get_employees()

    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
    for symbol in symbols:
        output = TA_Handler(symbol=symbol,
                            screener='Crypto',
                            exchange='Binance',
                            interval=Interval.INTERVAL_1_DAY)
        print('Рынок: ' + symbol)
        print(output.get_analysis().summary)
