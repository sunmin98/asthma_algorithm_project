import csv
import pandas as pd

f = open('asthma_dataset.csv', 'r', encoding='utf-8')
df = pd.read_csv('asthma_dataset.csv')
rdr = csv.reader(f)

for line in rdr:
    Asthma_symptom_lists = []
    try:
        Asthma_symptom_lists.extend(
            [int(line[7]), int(line[8]), int(line[9]), int(line[10]), int(line[11]), int(line[12]), int(line[13])])
    except:
        Asthma_symptom_lists.append('결측치')

    try:
        Asthma_symptom_score = sum(Asthma_symptom_lists)
        if Asthma_symptom_score < 20:
            print("조절이 안되는 상태")
            print("설문조사에 임하여 주세요")
            Check_symptom_frequency = int(input("얼마나 자주 천식 증상이 있었나요? [0. 전혀 그렇지 않았다. ~ 6. 항상 그랬다.]"))
            Check_unwellness = int(input("천식 증상으로 인하여 얼마나 불편하셨나요? [0. 전혀 그렇지 않았다. ~ 6. 심하게 그랬다.]"))
            Check_activity_severity = int(input("활동은 어떠셨나요? [0. 평소보다 잘했다. ~ 6. 평소보다 못했다.]"))
            Check_activity_difficulty = int(input("천식으로 인하여 자주 활동하는데 지장을 받았나요?"))
            Check_sleep_discoder = int(input("천식으로 인하여 어제 밤에 잠을 깨거나 오늘 아침에 평소보다 일찍 일어났나요? [0 ~ 3]"))
            Check_lists = [Check_symptom_frequency * 0.2, Check_unwellness * 0.2, Check_activity_severity * 0.5,
                           Check_activity_difficulty * 0.2, Check_sleep_discoder * 1.5]
            Check_lists_sum = sum(Check_lists)
            print(Check_lists_sum)

            average_last_2weeks = 5

            if average_last_2weeks < Check_lists_sum:
                flow_am = float(input("오전 최대호기유속 입력"))
                flow_pm = float(input("오후 최대호기유속 입력"))
                peak_flow_sum = flow_am + flow_pm
            else:
                print("신체에 이상 없음.")

            average_last_1weeks = 4

            if average_last_1weeks < peak_flow_sum:
                print("신체적 문제")

            else:
                print("정신적 문제")

            print(peak_flow_sum)
        elif 21 < Asthma_symptom_score:
            print("조절 근접 상태")
            print("설문조사에 임하여 주세요")
            Check_symptom_frequency = int(input("얼마나 자주 천식 증상이 있었나요? [0. 전혀 그렇지 않았다. ~ 6. 항상 그랬다.]"))
            Check_unwellness = int(input("천식 증상으로 인하여 얼마나 불편하셨나요? [0. 전혀 그렇지 않았다. ~ 6. 심하게 그랬다.]"))
            Check_activity_severity = int(input("활동은 어떠셨나요? [0. 평소보다 잘했다. ~ 6. 평소보다 못했다.]"))
            Check_activity_difficulty = int(input("천식으로 인하여 자주 활동하는데 지장을 받았나요?"))
            Check_sleep_discoder = int(input("천식으로 인하여 어제 밤에 잠을 깨거나 오늘 아침에 평소보다 일찍 일어났나요? [0 ~ 3]"))
            Check_lists = [Check_symptom_frequency * 0.2, Check_unwellness * 0.2, Check_activity_severity * 0.5,
                           Check_activity_difficulty * 0.2, Check_sleep_discoder * 1.5]
            Check_lists_sum = sum(Check_lists)
            print(Check_lists_sum)
            average_last_2weeks = 5

            if average_last_2weeks < Check_lists_sum:

                flow_am = float(input("오전 최대호기유속 입력"))
                flow_pm = float(input("오후 최대호기유속 입력"))
                peak_flow_sum = flow_am + flow_pm

            else:
                print("신체에 이상 없음.")

            average_last_1weeks = 4

            if average_last_1weeks < peak_flow_sum:
                print("신체적 문제")

            else:
                print("정신적 문제")

            print(peak_flow_sum)
        elif Asthma_symptom_score < 25:
            print("조절 달성 상태")
    except:
        print('결측치입니당')
