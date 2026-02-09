import streamlit as st

st.title("My First Streamlit App")

# สร้างแท็บ
tab1, tab2 = st.tabs(["Enter your name", "Calculator"])


# Tab 1: Enter your name
with tab1:
    st.write("Hello, Streamlit!")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Welcome, {name}!")

# Tab 2: Calculator
with tab2:
    st.title("Calculator")

    # แถวบน: ตัวเลข + ตัวดำเนินการ
    col1, col2, col3 = st.columns(3)

    with col1:
        num1 = st.number_input("First number", value=0.0)

    with col2:
        operation = st.selectbox(
            "Operation",
            ("Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)")
        )

    with col3:
        num2 = st.number_input("Second number", value=0.0)

    st.markdown("---")

    # ปุ่ม Calculate อยู่ตรงกลาง
    left, center, right = st.columns([4, 2, 4])
    with center:
        calculate = st.button("Calculate")

    # คำนวณและแสดงผล
    if calculate:
        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (×)":
            result = num1 * num2
        elif operation == "Divide (÷)":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                result = None
            else:
                result = num1 / num2

        if result is not None:
            st.success(f"Result: {result}")
