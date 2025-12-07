import random
import time

import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="Bubble Sort Visualizer",
    layout="wide",
)

st.title("🔵 Bubble Sort Visualizer")
st.write(
    "Generate a random list of 9 numbers and watch how "
    "**bubble sort** orders them step by step."
)

# --- Helpers (pure functions for logic & tests) ---

def generate_random_list(n: int = 9, low: int = 1, high: int = 50) -> list[int]:
    """Return a list of n random integers between low and high (inclusive)."""
    return [random.randint(low, high) for _ in range(n)]


def bubble_sort(numbers: list[int]) -> list[int]:
    """
    Pure bubble sort implementation.
    Returns a NEW sorted list and does not mutate the input.
    """
    arr = numbers[:]  # work on a copy
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# --- Initialize session state ---
if "numbers" not in st.session_state:
    st.session_state.numbers = []

# --- Layout ---
col_left, col_right = st.columns([1, 2])

with col_left:
    st.subheader("Controls")

    if st.button("🎲 Generate random list"):
        st.session_state.numbers = generate_random_list()
        st.success("New list generated!")

    sort_clicked = st.button("🔽 Sort with Bubble Sort")

with col_right:
    chart_placeholder = st.empty()

# --- Show current list (initially or after generation) ---
if st.session_state.numbers:
    with chart_placeholder.container():
        st.subheader("Current list")
        st.bar_chart(st.session_state.numbers)
        st.write(f"Values: {st.session_state.numbers}")
else:
    with chart_placeholder.container():
        st.subheader("Current list")
        st.write("Click **🎲 Generate random list** to start.")


# --- Bubble sort with animation for the UI ---
def bubble_sort_visual(numbers: list[int], placeholder, delay: float = 0.7) -> list[int]:
    """
    Bubble sort that MUTATES the list in-place and visualizes each step using Streamlit.
    Returns the same list object (now sorted), for convenience.
    """
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Show current comparison
            with placeholder.container():
                st.subheader("Bubble sort in progress…")
                st.write(f"Pass `{i + 1}`, comparing indices `{j}` and `{j + 1}`")
                st.bar_chart(numbers)
                st.write(f"Values: {numbers}")
            time.sleep(delay)

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

                with placeholder.container():
                    st.subheader("Bubble sort in progress… (after swap)")
                    st.write(
                        f"Swapped indices `{j}` and `{j + 1}` "
                        f"→ `{numbers[j]}`, `{numbers[j + 1]}`"
                    )
                    st.bar_chart(numbers)
                    st.write(f"Values: {numbers}")
                time.sleep(delay)

    with placeholder.container():
        st.subheader("✅ Sorting complete!")
        st.bar_chart(numbers)
        st.write(f"Sorted values: {numbers}")

    return numbers


# --- Handle sort button click ---
if sort_clicked:
    if not st.session_state.numbers:
        st.warning("Generate a list first using the 🎲 button.")
    else:
        # Make a copy for animation, then save result back
        nums = st.session_state.numbers[:]
        bubble_sort_visual(nums, chart_placeholder)
        st.session_state.numbers = nums
