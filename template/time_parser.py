note = []
s = "1:40"
e = "0:0"
parsed_s_time = s.split(':')
parsed_e_time = e.split(':')

if len(parsed_s_time[1]) != 2: 
    parsed_s_time[1] += "0"

if len(parsed_e_time[1]) != 2:
    parsed_e_time[1] += "0"

parsed_time = ':'.join(parsed_s_time) + " - " + ':'.join(parsed_e_time)
note.append(parsed_time)

print(note)
