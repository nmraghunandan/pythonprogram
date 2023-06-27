#Arport entering scenario
#Security checking for ticket validation

#Covid-19 testing Positive or negative
#if results positive not allowed to travel amount will be refunded

#imigration checking purpose of visiting, vaccination certificate and valid passport
 
#laguage weight chechking should be below 20kg, if there is more reduce the weight of laguaage or else not allowed
 
#boarding if all process are checked and passed then allow to flight:
print("*****Welcome to the Bengaluru international Airport*****")
name = input("You're good name : ").upper()
print(f"Hello, {name} please show the ticket")
ticket = input("Status of the ticket:\nValid or Invalid :  ").lower()         #Checking whether the ticket is valid or not.
if ticket == "valid":
    print("You're ticket is valid, please go in.")
    covid = input("Covid test report:\nPostive or Negative\n ").lower()       #Covid-19 resluts positive or negative.
    if covid == "positive":
        print("You're Covid-19 test are positive and you're not allowed to travel as per the rules")
        print("Please stay in home isolation and stay safe.\nThe ticket amount will be refunded.")
    elif covid == "negative":
        print("Good news, you're covid-19 results are negative\nPlease proceed with the further process")
        print("Please provide the vaccination certificate and the passport")
        documents = input("status of the documents:\nValid or Invalid ").lower()           #validating other documnets.
        if documents == "valid":
            purpose = input("What is the purpose of visiting:\nHoliday\nFamily_trip\nBusiness_trip\nOther\n").lower()    #Purpose of visiting.
            if purpose == "holiday" or purpose=="family_trip" or purpose=="business_trip":
                print("You're approved to travel, have a great journey.")
                laguage = int(input("Weight of the lagauge: "))                   #Weight of the lagauge.
                if laguage <= 20:
                    print(f"Weight of the laguage is {laguage}KG and approved to travel")
                    onboard = input("Is all the process are done?\nYes or No\n")             #Proceeding for onboarding.
                    if onboard == "yes":
                        print("You're onboard is scheduled good go. Have great journey")
                    else:
                        print("Please process the all checkings for onboarding")
                else:
                    print(f"The weight of the laguage is {laguage}KG. Please reduced it to below 20KG")
            else:
                print(f"Sorry, {name}\nYou're not allowed to travel")
    else:
        print("You're Covid-19 test results are awaited please stay here and take rest. Thank you") 
else:
    print(f"Sorry, {name} you're ticket is invalid. Please contact our heldesk.")
