---
title: 'Basic Excel: Level 1'
slug: excel-level-1
category: software
description: Let's open Excel together and get comfortable with cells, formatting, and your first real formula.
lead_in: 'Excel scares a lot of people, and I promise you it does not need to. In this lesson we will open it together and get comfortable with the basics: the cells, a little formatting, and your very first formula. By the end you will have built a real, working table with your own hands.'
video_url: ''
parts:
- title: Getting to know the Excel window
  blocks:
  - type: lesson
    title: What you are looking at
    body: |
      Let's open Excel and take a look around together. It can feel busy at first, so we will name the main parts. Once you know these, everything else gets easier.

      - **The Ribbon.** The strip of buttons across the top. It is grouped into tabs like Home, Insert, and Page Layout. Home is where you will spend most of your time.
      - **Cells.** The little boxes in the grid. Each one holds a piece of information.
      - **Columns and rows.** Columns go up and down and are labeled with letters (A, B, C). Rows go left and right and are labeled with numbers (1, 2, 3).
      - **The cell reference.** Every cell has an address made of its column letter and row number. The box where column B meets row 3 is cell **B3**.
      - **The Name Box and Formula Bar.** Just above the grid. The Name Box on the left shows which cell you are in. The Formula Bar shows what is inside it.

      > A **workbook** is the whole Excel file. Inside it, each **worksheet** is one grid, or tab, along the bottom. One workbook can hold several worksheets.
  - type: activity
    title: Find your way around
    body: |
      Open a blank workbook and try these, no rush:

      1. Click cell **B3**. Check that the Name Box shows "B3."
      2. Click the letter **C** at the top. The whole column highlights.
      3. Click the number **5** on the left. The whole row highlights.
      4. Find the Home tab on the Ribbon and just read the button names.

      That is it. You are already navigating a spreadsheet.
- title: Putting information in cells
  blocks:
  - type: lesson
    title: Type, edit, and move
    body: |
      Getting text and numbers into cells is the heart of Excel. Here is how.

      1. **Click a cell** to select it.
      2. **Type** your text or number.
      3. Press **Enter** to move down, or **Tab** to move right.

      To change what is already in a cell:

      - **Replace it:** click the cell and type something new.
      - **Edit part of it:** double-click the cell, then fix just the part you want.
      - **Clear it:** click the cell and press **Delete**.

      Two quick habits that save time:

      - **Copy and paste** with Ctrl+C and Ctrl+V.
      - **Undo** a mistake with Ctrl+Z. This one is your best friend. You can undo again and again.
- title: Making it look right
  blocks:
  - type: lesson
    title: Columns, rows, and formatting
    body: |
      Sometimes your text is too wide for its cell, or you want numbers to stand out. Let's fix the look.

      **Resize a column so text fits:**

      - Move your mouse to the line between two column letters at the top. The pointer becomes a two-way arrow.
      - Double-click that line to auto-fit, or click and drag to set the width by hand.

      Rows work the same way, using the lines between the row numbers.

      **Common formatting, all on the Home tab:**

      | Want to... | Do this |
      |---|---|
      | Make text bold | Click **B**, or press Ctrl+B |
      | Change the size or font | Use the font boxes on the Home tab |
      | Center text in a cell | Click the center-align button |
      | Add a background color | Use the paint-bucket (Fill) button |
      | Show numbers as money | Click the **$** button |

      The goal is a sheet that is easy to read at a glance. You do not need every button. A little bold and some space go a long way.
  - type: activity
    title: Build a small budget table
    body: |
      Let's make something real. In a blank sheet:

      1. In **A1**, type "Item." In **B1**, type "Cost."
      2. Fill in four rows below with items and amounts, like Groceries and 60.
      3. Make row 1 **bold**.
      4. Widen column A so the words fit.
      5. Select the cost numbers and click the **$** button.

      You just built and formatted a real table. Keep it open, we will add a formula to it next.
- title: Your first formula
  blocks:
  - type: lesson
    title: Let Excel do the math
    body: |
      Here is where Excel earns its keep. A **formula** is a math instruction, and every formula starts with an equals sign.

      Add two cells together:

      1. Click an empty cell.
      2. Type **=B2+B3** and press Enter.
      3. The cell shows the total. Change B2 or B3 and the total updates by itself.

      For a longer list, use **SUM**. It adds up a whole range for you:

      - Type **=SUM(B2:B5)** and press Enter.
      - That means "add everything from B2 down to B5."

      The magic part: because the formula points at cells, not fixed numbers, your totals stay correct when the numbers change. That is the whole reason people use Excel instead of a calculator.
  - type: activity
    title: Total your budget
    body: |
      Back to the table you built:

      1. Click the empty cell just below your cost numbers.
      2. Type **=SUM(** then click and drag over your cost cells, then type **)** and press Enter.
      3. Change one of the costs above and watch the total update on its own.

      If your total looks off, press Ctrl+Z and try again. That is normal, and it is how everyone learns this.
- title: Saving and printing
  blocks:
  - type: lesson
    title: Keep your work and share it
    body: |
      Let's make sure your work is safe and ready to hand off.

      **Save it:**

      - Press **Ctrl+S**, or click File, then Save.
      - The first time, pick a folder and give the file a clear name.
      - After that, Ctrl+S saves your latest changes in a second. Do it often.

      **Save a PDF** (a fixed picture of your sheet that anyone can open):

      - Click File, then **Save As** (or Export), and choose **PDF** in the file-type list.

      **Print it:**

      - Press **Ctrl+P** to open the print screen.
      - Use the preview on the right to check it fits nicely before you print.
  - type: quiz
    title: Quick check
    body: |
      When you are ready, take the short quiz. It covers the parts of the window, entering and formatting data, writing a SUM formula, and saving your work.

      I'll add the quiz link here once it is built. It opens in a new tab.
    quiz_url: ''
    quiz_label: Open the quiz
---
