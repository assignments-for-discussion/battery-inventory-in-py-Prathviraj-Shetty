
def count_batteries_by_health(present_capacities):
    SoH=[]
    # SoH list maintains the SoH value of each battery in percentage
    healthy_battery_count=0    #Maintains the healthy_battery_count
    exchange_battery_count=0    #Maintains the exchange_battery_count
    failed_battery_count=0  #Maintains the failed_battery_count
    for battery in present_capacities:
        cur_battery_SoH=100*battery/120
        SoH.append(cur_battery_SoH)
        #Classifying the batteries based on calculated SoH values int healthy,exchange and failed batteries
        if(cur_battery_SoH>80):
           healthy_battery_count=healthy_battery_count+1
        elif(cur_battery_SoH>=62 and cur_battery_SoH<=80):
           exchange_battery_count=exchange_battery_count+1
        else:
           failed_battery_count=failed_battery_count+1

    return {
    "healthy": healthy_battery_count,
    "exchange": exchange_battery_count,
    "failed": failed_battery_count
    }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")
    
def test_bucketing_by_health_2():
  print("Counting batteries by SoH...\n")
  #Here in this sample test case, we'll consider the present_capacities,i.e 96Ah,74.4Ah,0Ah and 120Ah that will give SoH values 80%,62%,0% and 100% respectively, to test for boundary conditions 
  present_capacities = [96, 6, 74.4, 0, 120, 90]
  counts = count_batteries_by_health(present_capacities)
  print(counts)
  assert(counts["healthy"] == 1)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
    test_bucketing_by_health_2()
