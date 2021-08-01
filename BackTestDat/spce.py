import csv
highest = []
heights = []
highest_gain = []
i = 0
ally = []
prices = []
all_gains = []
high_al = []
yo = []
yeet = []
list_of_options = ['GOOG  191122C01110000','GOOG  191122C01090000','GOOG  191122C01242500']
# list_of_options = ['GOOG  191122C01242500']
# with open('options_goog_23587_20191029.txt') as csv_file:
with open('spce.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    empty = []
    all_id = []
    certain_option = []
    big = []
    for row in csv_reader:
        # i += 1
        yo.append(row)
        # print(row)
    # print(yo)
    i = 0
    for x in yo:
        number = x[0]
        heights.append(number)
    # print(max(heights))
    
    for i in range(len(heights)):
    # print("TEST",option_id)
    # print(i)

        
        yup = []
        ally = []
        highest = []
        
            
        # for i in range(len(heights)):
        #     # print("TEST",option_id)
        #     # print(i)
        #     highest = []
        #     yup = []
        #     # try:
        wee = []
        new_highest = 0
        for j in range(i+1, len(heights)):
            # print(j)
            # print(heights[i])
            wee.append(heights[i])
            # print("wut",heights[j])
            # print("YES",max(wee))
            sell_out = float(max(wee))-(float(max(wee))*.10)
            # sell_out = float(max(wee))-(.13)
            # print("SELL OUT",sell_out)

            

            if heights[i] < heights[j] and float(heights[i]) > float(sell_out):
                
                # print("yes")

                yes = (((float(heights[j])/float(heights[i]))-1)*100).__round__(2)
                json = {"one":heights[i],"two":heights[j],"diff":yes}
                # print("YEAH",json)
                highest.append(json)
                wee.append(heights[j])
            else:
                pass
            # high.append(heights[j])
            # print("high",high)
        # print("highest",max(wee))
            # print("high",max(high))
            # print(highest)
            # print("highest",highest)

        for x in highest:
            high = x['diff']
            one = x['one']
            two = x['two']
            json = {"one":one,"two":two,"diff":high}
            # print(json)
            # print(json)
            ally.append(json)

        # print("ally",ally)
        for x in ally:
            diff = x['diff']
            yeet.append(diff)
        
        # print("MAx",max(yeet))
        for x in ally:
            if max(yeet) == x['diff']:
                print(x)
        # print("MAX",max(ally))
    res = {}
    for dic in ally:
        option_id = row[7]
        for key, val in dic.items():
            if key in res:
                # print(dic)
                res[key] = max(res[key], val)
                yo = res[key]
            else:
                res[key] = val
    
    for x in ally:
        if x['diff'] == res[key]:
            print(x)
            all_gains.append(x)
    
            

    # print("yo",yo)

# print(res[key])
        # price= row[6]
        # print(price)
        # call_or_put = row[5]
        # if call_or_put == 'C':
        #     empty.append(row)
        #     price = row[8]
        #     option_id = row[7]
        #     call_or_put = row[5]
        #     if option_id in all_id:
        #         pass
        #     else:
        #         all_id.append(option_id)
    # print(all_id)
    # i = 0
    # for x in all_id:
        
    #     i += 1
    #     # print(x)
    #     len_of_all = len(all_id)
    #     print(i,"of",len_of_all)
    #     # print(i)
    #     # print(x)
        
    #     highest = []
    #     for row in empty:
#         option_id = row[1]
#         print(option_id)
        

#         # x = x
#         # if x == option_id:

#         price = row[5]
#         # print(price)
#         json = {"price":price,"id":option_id}
#         prices.append(json)
#         # print("PRICES",prices)
#     print(prices)
#     for x in prices:
#         # print(x)
#         option_id = x['id']
#         # print("ID",option_id)
#         # print("yeet",option_id)
#         number = x['price']
#         if number == '':
#             real_number = 0
#         else:
#         # try:
#             real_number = float(number)
#         # real_number = 0
#         # print(real_number)
#         heights.append(real_number)
#     print(heights)
#     # print(heights)
    
#     hi = 0
#     # empty = []
#     ally = []
#     for i in range(len(heights)):
#         # print("TEST",option_id)
#         # print(i)
#         highest = []
#         yup = []
#         try:
#             for j in range(i+1, len(heights)):
#                 # print(j)
#                 if heights[i] < heights[j] :
#                     yes = (((heights[j]/heights[i])-1)*100).__round__(2)
#                     json = {"one":heights[i],"two":heights[j],"diff":yes}
#                     highest.append(json)
#                 else:
#                     pass
#             # print(highest)
#             # print("highest",highest)
#         except:
#             Exception
#         for x in highest:
#             high = x['diff']
#             one = x['one']
#             two = x['two']
#             json = {"id":option_id,"one":one,"two":two,"diff":high}
#             # print(json)
#             ally.append(json)
#         # print("ally",ally)
#     # prices.clear()
#     # highest.clear()
#     # heights.clear()
    
        
#     #     print("ally",ally)
#     #     for x in ally:
#     #         yeah = x['diff']
#     #         big.append(yeah)
#     #         print(yeah)
#     #     print("B IG",big)
#     #     print("MAX",max(big))
#     # print("big",big)
#     # print("MAX",max(big))
#     print(ally)
#     res = {}
#     for dic in ally:
#         option_id = row[7]
#         for key, val in dic.items():
#             if key in res:
#                 # print(dic)
#                 res[key] = max(res[key], val)
#             else:
#                 res[key] = val

#     print(res[key])

# try:
#     for x in ally:
#         if x['diff'] == res[key]:
#             print(x)
#             all_gains.append(x)
#             break
# except:
#     Exception
    

    
# #     print(len(list_of_options))
# #     prices.clear()
# #     ally.clear()
# # print(all_gains)
# # for x in all_gains:
# #     best = x['diff']
# #     high_al.append(best)
# # print("Best of best",max(high_al))
# # bestest = max(high_al)
# # for x in all_gains:
# #     if bestest == x['diff']:
# #         print("BEST GAIN",x,"%")
#     #     highest = max(prices)
#     #     lowest = min(prices)
#     #     print("higest",highest)
#     #     print("lowest",lowest)
#     #     try:
#     #         gain = (((float(highest)/float(lowest))-1)*100).__round__(2)
#     #         json = {"id":x,"highest_gain":gain}
#     #     except:
#     #         Exception
#     #         json = {"id":x,"highest_gain":0}
#     #     print(json)
#     #     highest_gain.append(json)
#     # print(highest_gain)
#     # for x in hello:
#     #     number = float(x)
#     #     print(number)
#     #     heights.append(number)
#     #     hi = 0
#     #     empty = []
#     #     ally = []
#     # for i in range(len(heights)):
#     #     print(i)
#     #     highest = []
#     #     yup = []
#     #     try:
#     #         for j in range(i+1, len(heights)):
#     #             print(j)
#     #             if heights[i] < heights[j]:
#     #                 yes = (((heights[j]/heights[i])-1)*100).__round__(2)
#     #                 json = {"one":heights[i],"two":heights[j],"diff":yes}
#     #                 highest.append(json)
#     #         print("highest",highest)
#     #     except:
#     #         Exception
#     #     for x in highest:
#     #         high = x['diff']
#     #         one = heights[i]
#     #         two = heights[j]
#     #         json = {"one":heights[i],"two":heights[j],"diff":high}
#     #         print(json)
#     #         ally.append(json)

#     # res = {}
#     # for dic in ally:
#     #     for key, val in dic.items():
#     #         if key in res:
#     #             res[key] = max(res[key], val)
#     #         else:
#     #             res[key] = val
#     # print("highest",res[key])
#     # print(hello)
