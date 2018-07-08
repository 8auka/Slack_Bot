from slackclient import SlackClient
import time
import requests
import pickle
import random
token = "xoxb-378644455970-395646296887-WiKB7yOUfafar57TR4mYOToW"
slack_client = SlackClient("xoxb-378644455970-395646296887-WiKB7yOUfafar57TR4mYOToW")
slack_client.rtm_connect()
#slack_client.rtm_send_message("bot_test", "Hi there")

api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    admins = []
    students = []
    #print(users)
    for user in users:
        if user.get('is_admin') == True:
            admins.append(user.get('name'))
        elif user.get('is_bot') == False:
            students.append(user.get('name'))

coins={}
with open('students.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % stud for stud in students)
def members():
    with open('students.txt') as file_content:
        slack_client.api_call(
            "files.upload",
            channels="bot_test",
            file=file_content,
            title="Test upload"
        )
for i in students:
    coins[i]= 0
def grouping():
    group=1
    s = []
    for i in range(len(students)) :
        s.append(students[i])
    st = s
    membersInGroup=4
    temp=[]
    sz = len(st)
    for i in range(sz):
        if membersInGroup==4:
            temp.append("Group {} consists of;".format(group))
            membersInGroup=0
            group+=1
        person=random.choice(st)
        temp.append(person)
        membersInGroup+=1
        st.remove(str(person))

    with open('groups.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % group for group in temp)
    with open('groups.txt') as file_content:
        slack_client.api_call(
            "files.upload",
            channels="bot_test",
            file=file_content,
            title="Test upload"
        )

while True:
    for slack_message in slack_client.rtm_read():
        message = slack_message.get("text")
        #user = slack_message.get("user")
        for user in users:
            if str(user.get('name')) =='baurzhansarsenov' and message =="//members":
                print("Members")
                members()
            elif str(user.get('name')) =='baurzhansarsenov' and message =="//groups":
                print("Grouping")
                grouping()
            elif not message or not user:
                continue
            #slack_client.rtm_send_message("bot_test", "<@{}> wrote something...".format(user))
    # Sleep for half a second
        time.sleep(0.5)
