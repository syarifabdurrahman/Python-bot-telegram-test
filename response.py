from datetime import datetime
import main as m
from Gempa_terkini import GempaTerkini

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup","halo","hola"):
        return "Hey!, How's it going?"

    if user_message in ("Who are you?","who are you"):
        return "I\'m Bot duh??"

    if user_message in("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    if user_message in ("bmkg", "gempa terkini"):
       gempa_di_indonesia = GempaTerkini()
       gempa_di_indonesia.ekstraksi_data()
       m.getURl(gempa_di_indonesia.get_img())

       

       return (gempa_di_indonesia.show_on_bot())

    return "I'm sorry, I don\'t understand"
    