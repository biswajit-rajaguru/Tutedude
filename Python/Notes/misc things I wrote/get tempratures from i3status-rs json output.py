import json

while True:
    s = input()
    s = s.strip(",\n")
    if not s:
        continue
    
    try:
        blocks = json.loads(s)
        if isinstance(blocks, list) and blocks:
            temprature_l = blocks[0]["full_text"].replace(","," ").split()
            #print(temprature_l)
            #temprature_l = [temp.strip() for temp in temprature_l if temp.strip()]
            #print(temprature_l)
            #tempratures = [int(temp.strip()) for temp in temprature_l if temp]
            tempratures = [int(temp) for temp in temprature_l]
             
            HOT, NORMAL, COLD, RESET = "\033[38;5;162m", "\033[38;5;107m", "\033[38;5;68m", "\033[0m"

            for temp in tempratures:
                if temp < 40:
                    color = COLD
                elif temp < 50:
                    color = NORMAL
                else:
                    color = HOT
                print(f"{color}{temp}{RESET}", end = " ")
            print()
            
    except json.JSONDecodeError as e:
        #print(f"(ERROR JSON)e")
        continue
    except IndexError:
        #print("Error IndexError")
        continue
    except KeyError:
        #print("Error KeyError")
        continue
    except ValueError as e:
        #print(f"Error ValueError {e}")
        continue



