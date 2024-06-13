def solution(records):
    id_name = {}
    message = []
    
    for record in records:
        action = record.split()[0]
        
        if action == 'Enter':
            action, ID, name = record.split()
            id_name[ID] = name
            message.append([ID, '님이 들어왔습니다.'])
            
        elif action == 'Leave':
            action, ID = record.split()
            message.append([ID, '님이 나갔습니다.'])
        
        else:
            action, ID, name = record.split()
            id_name[ID] = name

    for m in range(len(message)):
        message[m][0] = id_name[message[m][0]]
        message[m] = ''.join(message[m])
      
    return message