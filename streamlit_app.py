import streamlit as st
import json
import copy

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data():
    with open("data.json", "w") as f:
        json.dump(st.session_state.plan_list, f)

if "plan_list" not in st.session_state:
    try :
        st.session_state.plan_list = load_data()
    except :
        st.session_state.plan_list = {"main" : []}

# Side panel for chat selection and options
with st.sidebar:
    st.header("Your Plans")
    selected_chat = st.radio(
        "Select a Routine",
        st.session_state.plan_list,
        #format_func=lambda x: x.capitalize(),
        #index=2  # Assuming new_chat3 should be the default selection
    )

    st.header("Create new")
    # language = st.selectbox('Select language', ['English', 'korean', 'japanese'])
    # level = st.selectbox('Your level', ['beginner', 'intermediate', 'advanced'])
    title = st.text_input('Write your topic')
    new_chat = st.button('Start!')
    delete_chat = st.button('Delete this plan')
    copy_chat = st.button('Copy this plan')

    #openai_api_key = st.text_input("OpenAI API Key", type="password")
    #bing_api_key = st.text_input("bing API Key", type="password")

    if new_chat:
        # Add the new chat to the list if the topic is not empty
        if title:
            if title in st.session_state.plan_list :
                st.warning("Plan already exists. Please choose another title!")
            else :
                st.session_state.plan_list[title] = [{"aero" : {"title" : "not defined", "link" : ""}, 
                                                      "ara" : {"title" : "not defined", "link" : ""}} 
                                                      for i in range(7)]
        else:
            st.warning("Please write a title before starting a new plan!")

    if delete_chat:
        st.session_state.plan_list.remove(selected_chat)
    if copy_chat :
        if title in st.session_state.plan_list :
            st.warning("Plan already exists. Please choose another title!")
        else :
            st.session_state.plan_list[title] = copy.deepcopy(st.session_state.plan_list[selected_chat])


# Display the selected chat


# Main chat window
st.header(selected_chat.capitalize())

# if selected_chat == 'main' :
#     st.write("This is chatbot that can be used to learn another language.",
#              "Make new chatting with left header.",
#              "You can input the topic you are interested in, and you can choose your language level.")
#     st.write("beginner : If you send text in english, it would translate it into selected language.")
#     st.write("intermediate / advanced : It is option for people who can free-talk in selected language. chatbot would fix your sentences more naturally.")
#     placeholder = st.empty()
#     st.write("You can also fix prompt in the \"option\" tab.")

    

if selected_chat != 'main' :
    plan, editor = st.tabs(['Plan viewer', 'Editor'])

    with plan :
        columns = st.columns([1,1,1,1,1,1,1])

        days = ["" for i in range(7)]
        with columns[0] :
            days[0] = st.button("Mon")
        with columns[1] :
            days[1] = st.button("Tue")
        with columns[2] :
            days[2] = st.button("Wed")
        with columns[3] :
            days[3] = st.button("Thu")
        with columns[4] :
            days[4] = st.button("Fri")
        with columns[5] :
            days[5] = st.button("Sat")
        with columns[6] :
            days[6] = st.button("Sun")

        if days[0] :
            st.write(st.session_state.plan_list[selected_chat][0]['aero']['title'])
            st.video(st.session_state.plan_list[selected_chat][0]['aero']['link'])
            st.write(st.session_state.plan_list[selected_chat][0]['ara']['title'])
            st.video(st.session_state.plan_list[selected_chat][0]['ara']['link'])
        if days[1] :
            st.write(st.session_state.plan_list[selected_chat][1]['aero']['title'])
            st.video(st.session_state.plan_list[selected_chat][1]['aero']['link'])
            st.write(st.session_state.plan_list[selected_chat][1]['ara']['title'])
            st.video(st.session_state.plan_list[selected_chat][1]['ara']['link'])
        if days[2] :
            st.write(st.session_state.plan_list[selected_chat][2]['aero']['title'])
            st.video(st.session_state.plan_list[selected_chat][2]['aero']['link'])
            st.write(st.session_state.plan_list[selected_chat][2]['ara']['title'])
            st.video(st.session_state.plan_list[selected_chat][2]['ara']['link'])
        if days[3] :
            st.write(st.session_state.plan_list[selected_chat][3]['aero']['title'])
            st.video(st.session_state.plan_list[selected_chat][3]['aero']['link'])
            st.write(st.session_state.plan_list[selected_chat][3]['ara']['title'])
            st.video(st.session_state.plan_list[selected_chat][3]['ara']['link'])
        if days[4] :
            st.write(st.session_state.plan_list[selected_chat][4]['aero']['title'])
            st.video(st.session_state.plan_list[selected_chat][4]['aero']['link'])
            st.write(st.session_state.plan_list[selected_chat][4]['ara']['title'])
            st.video(st.session_state.plan_list[selected_chat][4]['ara']['link'])
        if days[5] :
            st.write(st.session_state.plan_list[selected_chat][5]['aero']['title'])
            st.video(st.session_state.plan_list[selected_chat][5]['aero']['link'])
            st.write(st.session_state.plan_list[selected_chat][5]['ara']['title'])
            st.video(st.session_state.plan_list[selected_chat][5]['ara']['link'])
        if days[6] :
            st.write(st.session_state.plan_list[selected_chat][6]['aero']['title'])
            st.video(st.session_state.plan_list[selected_chat][6]['aero']['link'])
            st.write(st.session_state.plan_list[selected_chat][6]['ara']['title'])
            st.video(st.session_state.plan_list[selected_chat][6]['ara']['link'])
            


    with editor :
        st.write("edit box will be here")
        dayselected = st.selectbox("day", ["select", "mon", "tue", "wed", "thu", "fri", "sat", "sun"])
        fixbox = [st.columns([1,3]) for i in range(4)]
        if dayselected != "select" :
            daylist = {"mon" : 0, "tue" : 1, "wed" : 2, "thu" : 3, "fri" : 4, "sat" : 5, "sun" : 6 }
            num = daylist[dayselected]

            with fixbox[0][0] :
                st.session_state.plan_list[selected_chat][num]['aero']['title'] = st.text_input("aero_title")
            with fixbox[0][1] :
                st.session_state.plan_list[selected_chat][num]['aero']['link'] = st.text_input("aero_link")
            with fixbox[1][0] :
                st.session_state.plan_list[selected_chat][num]['ara']['title'] = st.text_input("ara_title")
            with fixbox[1][1] :
                st.session_state.plan_list[selected_chat][num]['ara']['link'] = st.text_input("ara_link")

            save = st.button("save")

            if save :
                save_data()

            st.write(dayselected," :")
            st.write("aero : " , st.session_state.plan_list[selected_chat][num]['aero']['title'])
            st.write("ara : " , st.session_state.plan_list[selected_chat][num]['ara']['title'])


