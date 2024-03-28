
count = 0
progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
list_part2 = []
list_part2a = []

def part_a ():
    global count
    
    total = 0
    list_1 = [0, 20, 40, 60, 80, 100, 120]
    
    
# PASS CREDIT
    pass_credit = input('Please enter your credits at pass: ') 

    while True :
        try :
            x = int(pass_credit)
        
            if x not in list_1 :
                print ('Out of range.')
                print
                part_a()
                break
            elif x in list_1:
                total = total + x

                # DEFER CREDIT
                defer_credit = input('Please enter your credits at defer: ')

                while True :
                    try :
                        y = int(defer_credit)
                        if not y in list_1 :
                            print ('Out of range.')
                            print('')
                            part_a()
                            break
                        elif y in list_1 :
                            total = total + y
                
                            # FAIL CREDIT   
                            fail_credit = input('Please enter your credits at fail: ')

                            while True :
                                try :
                                    z = int(fail_credit)
        
                                    if not z in list_1 :
                                        print ('Out of range.')
                                        print('')
                                        part_a()
                                        break
            
                                    elif z in list_1 :
                                        total_all = total + z

                                            
                                except ValueError :
                                    print ('Integer required. Please try again.')
                                    part_a()
    
                                    break
                             

                                # TRY AGAIN, QUIT OR CONTINUE THE PROGRAM 
                                    
                                while True :

                                    if total_all != 120 :
                                        print('')
                                        print('Total incorrect.')
                                        print ('')
                                        part_a()

                                    elif total_all == 120 :
                                        print('')
                                        count += 1
                                  

                                 # PROGRESSION OUTCOME
                                
                                        while True:
                                    
                                            if x == 120 :
                                                print('Progress')
                                                global progress
                                                global list_part2a
                                                progress += 1
                                                list_part2.append('Progress - '+ pass_credit + ',' + defer_credit + ',' + fail_credit )
                                                list_part2a = '\n'.join(list_part2)

                                            elif x == 100 :
                                                print('Progress (module trailer)')
                                                global module_trailer
                                                module_trailer += 1
                                                list_part2.append('Progress (module trailer) - '+ pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                list_part2a = '\n'.join(list_part2)
                                               
                                                
                                            elif x == 80 :
                                                print ('Do not progress - module retriever')
                                                global module_retriever
                                                module_retriever += 1
                                                list_part2.append('Module retriever - '+ pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                list_part2a = '\n'.join(list_part2)
                                                
                                            elif x == 60 :
                                                print ('Do not progress - module retriever')
                                                module_retriever += 1
                                                list_part2.append('Module retriever - '+ pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                list_part2a = '\n'.join(list_part2)
                                                
                                            elif x == 40 :
                                                if y == 0 and z == 80:
                                                    print ('Exclude')
                                                    global exclude
                                                    exclude += 1
                                                    list_part2.append('Exclude - '+ pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                    list_part2a = '\n'.join(list_part2)
                                                
                                                else :
                                                    print ('Do not progress - module retriever')
                                                    module_retriever += 1
                                                    list_part2.append('Module retriever - '+ pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                    list_part2a = '\n'.join(list_part2)
                                                    
                                            elif x == 20:
                                                if y <= 20 :
                                                    print ('Exclude')
                                                    exclude += 1
                                                    list_part2.append('Exclude - ' + pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                    list_part2a = '\n'.join(list_part2)
                                                
                                                else :
                                                    print ('Do not progress - module retriever')
                                                    module_retriever += 1
                                                    list_part2.append('Module retriever - ' + pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                    list_part2a = '\n'.join(list_part2)
                                                
                                            elif x == 0 :
                                                if y <= 40 :
                                                    print ('Exclude')
                                                    exclude += 1
                                                    list_part2.append('Exclude - ' + pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                    list_part2a = '\n'.join(list_part2)
                                                
                                                else :
                                                    print ('Do not progress - module retriever')
                                                    module_retriever += 1
                                                    list_part2.append('Module retriever - '+ pass_credit + ',' + defer_credit + ',' + fail_credit)
                                                    list_part2a = '\n'.join(list_part2)
                                                
                                            break
                                        
                                        print('')
                                        quit_1 = str(input ('Enter "q" to quit or press "enter" to continue. \n'))
                                    
                                        if quit_1 == 'q' :
                                            print ('')
                                            print('Thanks for using the program, have a good day!')
                                            
                                            break
                                    
                                    
                                        else:
                                            print('')
                                            part_a()
                                    break
                                break
                    
                    except ValueError :
                        print ('Integer required. Please try again.')
                        part_a()
                        break
                    
                    break

        except ValueError :
            print ('Integer required. Please try again.')
            part_a()
        break
    


part_a()

#PART 2
print (list_part2a)

#PART 3      
with open('part3.txt' , 'w') as f :
    f.write (list_part2a)


# HISTOGRAM

from graphics import *

results = {
    'Progress' : progress ,
    'Trailer' : module_trailer ,
    'Retriever' : module_retriever ,
    'Excluded' : exclude ,
}

max_value = max(results.values())
scale = 100 / max_value

win = GraphWin("Histogram", 800, 800)
win.setBackground ('whitesmoke')

header = Text(Point(400, 110), 'Histogram Results')
header.setFace('times roman')
header.setSize(25)
header.setStyle('bold')
header.draw(win)

outcome = Text(Point(160, 550), count)
outcome.setFace('times roman')
outcome.setSize(20)
outcome.setStyle('bold')
outcome.draw(win)

text1 = Text(Point(250, 550), 'outcomes in total')
text1.setFace('times roman')
text1.setSize(20)
text1.setStyle('bold')
text1.draw(win)

line1 = Line(Point(200, 400), Point(600, 400))
line1.draw(win)

def progress_grph (): 
    x1 = 205
    y1 = 400
    x2 = 295
    y2 = 400 - (progress) * (scale)
        
    bar = Rectangle(Point(x1, y1), Point(x2, y2))
    bar.setFill("mediumseagreen")
    bar.draw(win)
    p_text = Text(Point(255, 420), 'Progress')
    p_text.setFace('times roman')
    p_text.setSize(15)
    p_text.draw(win)

    number_progress = Text(Point(255, y2-50), progress)
    number_progress.setFace('times roman')
    number_progress.setSize(15)
    number_progress.draw(win)

def trailer_grph (): 
    x1 = 305
    y1 = 400
    x2 = 395
    y2 = 400 - (module_trailer) * (scale)
        
    bar = Rectangle(Point(x1, y1), Point(x2, y2))
    bar.setFill("palegoldenrod")
    bar.draw(win)
    p_text = Text(Point(355, 420), 'Trailer')
    p_text.setFace('times roman')
    p_text.setSize(15)
    p_text.draw(win)

    number_trailer = Text(Point(355, y2-50), module_trailer)
    number_trailer.setFace('times roman')
    number_trailer.setSize(15)
    number_trailer.draw(win)
    
def retriever_grph (): 
    x1 = 405
    y1 = 400
    x2 = 495
    y2 = 400 - (module_retriever) * (scale)
        
    bar = Rectangle(Point(x1, y1), Point(x2, y2))
    bar.setFill("sandybrown")
    bar.draw(win)
    p_text = Text(Point(455, 420), 'Retriever')
    p_text.setFace('times roman')
    p_text.setSize(15)
    p_text.draw(win)

    number_retriever = Text(Point(455, y2-50), module_retriever)
    number_retriever.setFace('times roman')
    number_retriever.setSize(15)
    number_retriever.draw(win)

def exclude_grph (): 
    x1 = 505
    y1 = 400
    x2 = 595
    y2 = 400 - (exclude) * (scale)
        
    bar = Rectangle(Point(x1, y1), Point(x2, y2))
    bar.setFill("indianred")
    bar.draw(win)
    p_text = Text(Point(555, 420), 'Exclude')
    p_text.setFace('times roman')
    p_text.setSize(15)
    p_text.draw(win)

    number_exclude = Text(Point(555, y2-50), exclude)
    number_exclude.setFace('times roman')
    number_exclude.setSize(15)
    number_exclude.draw(win)

progress_grph()
trailer_grph()
retriever_grph()
exclude_grph()



