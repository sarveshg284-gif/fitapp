import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="To-Do List",
    page_icon="📝",
    layout="centered"
)

# -----------------------------
# Session State
# -----------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# -----------------------------
# Functions
# -----------------------------
def add_task():
    task = st.session_state.new_task.strip()

    if task:
        st.session_state.tasks.append(
            {
                "task": task,
                "completed": False
            }
        )
        st.session_state.new_task = ""
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")


# -----------------------------
# Title
# -----------------------------
st.title("📝 TO-DO LIST")
st.write("Manage your daily tasks efficiently.")

st.divider()

# -----------------------------
# Add Task
# -----------------------------
st.subheader("➕ Add New Task")

st.text_input(
    "Task",
    key="new_task",
    placeholder="Enter your task here..."
)

st.button(
    "Add Task",
    on_click=add_task,
    use_container_width=True
)

st.divider()

# -----------------------------
# Display Tasks
# -----------------------------
st.subheader("📋 Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks available.")
else:
    for i, task in enumerate(st.session_state.tasks):

        with st.container():

            col1, col2 = st.columns([7, 3])

            with col1:
                completed = st.checkbox(
                    task["task"],
                    value=task["completed"],
                    key=f"check_{i}"
                )

                st.session_state.tasks[i]["completed"] = completed

            with col2:
                if st.button("✏ Edit", key=f"edit_{i}"):
                    st.session_state[f"editing_{i}"] = True

                if st.button("🗑 Delete", key=f"delete_{i}"):
                    st.session_state.tasks.pop(i)
                    st.rerun()

            # -----------------------------
            # Edit Task
            # -----------------------------
            if st.session_state.get(f"editing_{i}", False):

                updated_task = st.text_input(
                    "Edit Task",
                    value=task["task"],
                    key=f"text_{i}"
                )

                save_col, cancel_col = st.columns(2)

                with save_col:
                    if st.button("💾 Save", key=f"save_{i}"):

                        if updated_task.strip():
                            st.session_state.tasks[i]["task"] = updated_task.strip()

                        st.session_state[f"editing_{i}"] = False
                        st.rerun()

                with cancel_col:
                    if st.button("Cancel", key=f"cancel_{i}"):

                        st.session_state[f"editing_{i}"] = False
                        st.rerun()

            st.divider()

# -----------------------------
# Statistics
# -----------------------------
if st.session_state.tasks:

    total = len(st.session_state.tasks)
    completed = sum(task["completed"] for task in st.session_state.tasks)
    pending = total - completed

    st.subheader("📊 Task Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total", total)
    col2.metric("Completed", completed)
    col3.metric("Pending", pending)

    st.progress(completed / total)

# -----------------------------
# Clear All Tasks
# -----------------------------
st.divider()

if st.button(
    "🧹 Clear All Tasks",
    use_container_width=True
):
    st.session_state.tasks.clear()

    # Remove editing flags
    for key in list(st.session_state.keys()):
        if key.startswith("editing_"):
            del st.session_state[key]

    st.success("All tasks cleared successfully!")
    st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Developed using Python 🐍 and Streamlit 🚀")
