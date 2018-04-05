class Call(object):
    def __init__(self, unique_id, caller_name, caller_pn, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_pn = caller_pn
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display_all(self):
        print self.unique_id
        print self.caller_name
        print self.caller_pn
        print self.time_of_call
        print self.reason_for_call
        return self

class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue_size = 0
    def add_call(self, call):
        self.call_list.append(call)
        self.queue_size += 1
        return self
    def add_calls(self,*calls):
        for call in calls:
            self.call_list.append(call)
        self.queue_size = len(self.call_list)
        return self
    def remove_call(self):
        self.call_list.pop(0)
        self.queue_size -= 1
        return self
    def info(self):
        d=sorted(self.call_list, key=lambda call: call.time_of_call)  
        for i in range(0, len(d)):
            a=d[i].time_of_call
            b=d[i].caller_name
            c=d[i].caller_pn
            print a, b, c
        return self

call1=Call(1, "Andy Moon", "214.502.0617", "8:41pm", "my code won't work")
call2=Call(2, "Blake Moon", "214.214.2144", "1:44pm", "Gavin took my Legos")
call3=Call(3, "Gavin Moon", "972.972.9722", "9:00am", "Blake took my Legos")
call4=Call(4, "Julie Moon", "817.817.8177", "2:19pm", "I need a nap")

dojo=CallCenter()

# print call1.caller_name
# call1.display_all()
# dojo.add_call(call1)
# dojo.add_call(call2)
# print dojo.call_list[0].caller_name
# print dojo.call_list[1].caller_name
# print dojo.call_list[0].caller_pn
dojo.add_calls(call1,call2,call3)
dojo.add_call(call4)
# dojo.remove_call()
print dojo.queue_size
# print dojo.call_list
print dojo.info()
