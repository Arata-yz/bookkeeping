# 仕訳処理の基本クラス
class Account:
  def __init__(self) -> None:
    self.layors = []

  # 仕訳1行追加
  def write(self, date,
            debit_name:str,
            credit_name:str,
            amount:int,
            count:int = 1
            ) -> object:

    self.layors.append({
      'seqnr': len(self.layors) + 1, # 通し番号
      'date': date, # 日付
      'debit_name': debit_name, # 借方科目
      'credit_name': credit_name, # 貸方科目
      'amount': amount, # 金額
      'count': count # 同一仕訳内の連番
      })
    return self

  # 台帳出力
  def summary(self):
    print('=================================================================')
    for x in self.layors:
      if x['count']==1:
        date = x['date']
        print(f'|| {date} ||')
      a=x['debit_name']
      b=x['amount']
      c=x['credit_name']
      d=x['amount']
      print(f'| {a} {b:10} | {c} {d:10} |')
    print('=================================================================')
