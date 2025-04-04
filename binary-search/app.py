import streamlit as st
import numpy as np
import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = []
    
    while left <= right:
        mid = (left + right) // 2
        steps.append((left, mid, right))
        
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, steps

def main():
    st.title("🔍 Binary Search Visualizer")
    
    st.sidebar.header("⚙️ Settings")
    array_size = st.sidebar.slider("📏 Array Size", min_value=5, max_value=50, value=10)
    target = st.sidebar.number_input("🎯 Target Value", value=5, step=1)
    
    arr = sorted(np.random.randint(1, 100, size=array_size))
    st.write("### 📊 Sorted Array:", arr)
    
    if st.button("▶️ Run Binary Search"):
        index, steps = binary_search(arr, target)
        
        for step in steps:
            left, mid, right = step
            st.write(f"🔎 Checking: left={left}, mid={mid}, right={right}, value={arr[mid]}")
            time.sleep(0.5)  # Slow down for visualization
        
        if index != -1:
            st.success(f"✅ Found {target} at index {index}")
        else:
            st.error(f"❌ {target} not found in the array")

if __name__ == "__main__":
    main()


# ایک ترتیب شدہ (Sorted) لسٹ بنتی ہے

#numpy کا استعمال کرکے رینڈم نمبرز لیے جاتے ہیں اور ان کو چھوٹے سے بڑے ترتیب میں رکھ دیا جاتا ہے۔

#یہ لسٹ اسکرین پر دکھائی جاتی ہے۔

#صارف سے ان پٹ لی جاتی ہے

#سائیڈ بار میں سلائیڈر ہے جس سے لسٹ کا سائز منتخب کر یک عدد انٹر کرنے کا آپشن ہے#جو وہ نمبر ہے جس کو لسٹ میں تلاش کرنا ہ۔بائنری سرچ چلائی جاتی ہے

#بٹن "Run Binary Search" دبانے پر بائنری سرچ شروع ہوتی ہے۔


#پہلے لسٹ کے درمیانی (Middle) عنصر کو چیک کیا جاتا ہے۔

#اگر وہ نمبر ہدف (Target) کے برابر ہو تو جواب مل جاتا ہے
#و سبز (✅) پیغام آتا ہے کہ "نمبر مل گیا!"

#اگر نہ ملے تو سرخ (❌) پیغام آتا ہے کہ "نمبر نہیں ملا!"

#📌 مختصر میں:
#یہ پروجیکٹ ترتیب شدہ نمبرز کی لسٹ میں تیزی سے تلاش کرنے کے طریقے کو ویژولائز (دکھانے) کے لیے بنایا گیا ہے۔ 🚀