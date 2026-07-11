import streamlit as st

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.set_page_config(page_title="To-Do List", page_icon="📝")

st.title("📝 TO-DO LIST")

# Add Task
task = st.text_input("Enter a new task")

if st.button("➕ Add Task"):
    if task.strip():
        st.session_state.tasks.append(
            {"task": task, "completed": False}
        )
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

st.divider()

st.subheader("Your Tasks")

# Display Tasks
if st.session_state.tasks:
    for i, item in enumerate(st.session_state.tasks):

        col1, col2, col3 = st.columns([6, 2, 2])

        with col1:
            if item["completed"]:
                st.markdown(f"~~{item['task']}~~ ✅")
            else:
                st.write(item["task"])

        with col2:
            if not item["completed"]:
                if st.button("✔ Complete", key=f"complete{i}"):
                    st.session_state.tasks[i]["completed"] = True
                    st.rerun()

        with col3:
            if st.button("🗑 Delete", key=f"delete{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

else:
    st.info("No tasks added yet.")

st.divider()

# Clear All Tasks
if st.button("🧹 Clear All Tasks"):
    st.session_state.tasks.clear()
    st.success("All tasks cleared!")
    st.rerun()
