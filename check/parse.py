#-*- coding:utf-8 -*-

from .models import item

def parse(filename):
#    f = open(filename,'r',encoding='utf8')
	# 결과값: 정상, 업데이트, 숫자이상, 필드이상
    results = {'normal': 0, 'update': 0, 'valueerror': 0, 'fielderror': 0}

    f = open(filename,'r')
    with f:
        rows = f.readlines()[3:]
        errors = []
        for row in rows:
            #?문자 발생시 구분기호로 변경
            row = row.replace('?','|')
            data = [x.strip() for x in row.split('|')][1:-1]
            if len(data) == 20:
                #수량 이상 시 이상표시
                try:
                    data[8] = int(data[8])
					results['nornal'] = results['normal'] + 1
                except ValueError:
                    data[8] = '9999'
					results['valueerror'] = results['valueerror'] + 1
                    errors.append(data)
                
                querySet = item.objects.filter(no = data[0])
                if querySet.exists() == False:
                    db = item(no = data[0],
                            group = data[1],
                            name = data[2],
                            description = data[3],
                            slot = data[4],
                            oldNo = data[5],
                            groupText = data[6],
                            safetyAmount = data[7],
                            amount = data[8],
                            buyAmount = data[9],
                            totalAmount = data[10],
                            itemType = data[11],
                            BUn = data[12],
                            price = float(data[13].replace(',','')),
                            totalPrice = float(data[14].replace(',','')),
                            Pe = data[15],
                            Plnt = data[16],
                            Sloc = data[17],
                            itemGroup = data[18],
                            itemUsage = data[19]
                    )
                    db.save()
                else:
                    querySet[0].amount = data[8]
                    querySet[0].save()
					results['update'] = results['update'] + 1
            else:
				results['fielderror'] = results['fielderror'] + 1
                errors.append(data)

    return errors
