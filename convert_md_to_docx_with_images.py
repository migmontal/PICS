#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def markdown_to_docx_with_images(md_file, docx_file, image_dir='forest_plots'):
    doc = Document()

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    in_table = False
    table_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()

        # Handle images: [Image: path/to/image.png]
        if '[Image:' in line_stripped:
            match = re.search(r'\[Image:\s*([^\]]+)\]', line_stripped)
            if match:
                img_path = match.group(1).strip()
                if os.path.exists(img_path):
                    p = doc.add_paragraph()
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = p.add_run()
                    run.add_picture(img_path, width=Inches(6))
            i += 1
            continue

        if not line_stripped:
            i += 1
            continue

        if line_stripped.startswith('# '):
            p = doc.add_heading(line_stripped[2:], level=1)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif line_stripped.startswith('## '):
            doc.add_heading(line_stripped[3:], level=2)
        elif line_stripped.startswith('### '):
            doc.add_heading(line_stripped[4:], level=3)
        elif line_stripped.startswith('#### '):
            doc.add_heading(line_stripped[5:], level=4)
        elif line_stripped == '---':
            doc.add_paragraph()
        elif line_stripped.startswith('|'):
            if not in_table:
                in_table = True
                table_lines = [line_stripped]
            else:
                table_lines.append(line_stripped)
        elif in_table and line_stripped.startswith('|'):
            table_lines.append(line_stripped)
        else:
            if in_table:
                create_table(doc, table_lines)
                in_table = False
                table_lines = []

            text = process_markdown_text(line_stripped)
            if line.startswith('- '):
                p = doc.add_paragraph(text[2:], style='List Bullet')
            elif line.startswith('  -'):
                p = doc.add_paragraph(text[4:], style='List Bullet 2')
            else:
                p = doc.add_paragraph(text)

        i += 1

    if in_table:
        create_table(doc, table_lines)

    doc.save(docx_file)
    print(f"Document saved: {docx_file}")

def process_markdown_text(text):
    # Remove bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    # Remove italics
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    # Remove code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Keep citations as is [1], [2], etc.
    return text

def create_table(doc, table_lines):
    if len(table_lines) < 2:
        return

    header = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]

    num_cols = len(header)
    table = doc.add_table(rows=1, cols=num_cols)
    table.style = 'Light Grid Accent 1'

    hdr_cells = table.rows[0].cells
    for i, cell_text in enumerate(header):
        hdr_cells[i].text = cell_text.replace('---', '').strip()

    for line in table_lines[2:]:
        if line.startswith('|'):
            row_cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if len(row_cells) == num_cols:
                row = table.add_row()
                for i, cell_text in enumerate(row_cells):
                    row.cells[i].text = cell_text

if __name__ == '__main__':
    markdown_to_docx_with_images('PICS_SR_MA_BMC_READY.md', 'PICS_SR_MA_BMC_READY.docx')
