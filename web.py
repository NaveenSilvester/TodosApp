import streamlit as st
import function
todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todo = todo+"\n"
    todos.append(todo)
    function.write_todos(todos)




st.title("My Todo App")
st.subheader("This is my subheader")
st.write("This app is to improve your productivity")
#FILEPATH = "todos.txt"
#todos = function.get_todos("todos.txt")
for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

#for item in todos:
#    st.checkbox(item)


st.text_input(label="Enter your Todos", placeholder="Enter your next todo...",
                 on_change=add_todo, key="new_todo")

st.session_state