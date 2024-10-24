import re

# Translating Japanese course names to English
course_translation = {
    "自然科学総論Ⅰ": "General Natural Sciences I",
    "放射線防護学特論": "Topics in Radiation Protection",
    "数理計画概論": "Introduction to Mathematical Programming",
    "機能性表面特論": "Advanced Functional Surfaces",
    "宇宙探査ロボティクス特論": "Space Exploration Robotics",
    "ネットワーク・セキュリティ特論": "Advanced Networks and Security",
    "移動情報ネットワーク特論": "Advanced Mobile Information Networks",
    "ソフトウエア構成論特論": "Software Construction",
    "産業スペシャリスト育成特論": "Training Course for Industrial Specialists",
    "技術・社会システム工学総論": "Science, Technology and Society, General",
    "コミュニケーション支援特論": "Assistive Technology for Communication",
    "ビジネス英語": "Business English",
    "地盤防災論": "Geotechnical Disaster Management",
    "集中日本語０ G": "Intensive Japanese 0",
    "西洋言語概説": "Lecture on Western Languages",
    "自然科学総論Ⅰ": "General Natural Sciences I",
    "宇宙探査ロボティクス特論": "Space Exploration Robotics"
}




# Period times
period_times = {
    "1限": ("083000", "100000"),
    "2限": ("101500", "114500"),
    "3限": ("125500", "142500"),
    "4限": ("144000", "161000"),
    "5限": ("162500", "175500")
}

# Function to update event summary and add timestamps for periods
def update_ics(file_content):
    lines = file_content.splitlines()
    updated_lines = []
    event_block = []
    in_event = False

    for line in lines:
        if line.startswith("BEGIN:VEVENT"):
            in_event = True
            event_block = [line]
        elif line.startswith("END:VEVENT"):
            in_event = False
            event_block.append(line)
            
            # Process the complete event block
            updated_block = process_event_block(event_block)
            updated_lines.extend(updated_block)
        elif in_event:
            event_block.append(line)
        else:
            updated_lines.append(line)
    
    return "\n".join(updated_lines)

# Function to process each event block
def process_event_block(event_block):
    updated_block = []
    period = None
    for line in event_block:
        # Translate course name in SUMMARY
        if line.startswith("SUMMARY:"):
            for japanese, english in course_translation.items():
                if japanese in line:
                    line = line.replace(japanese, english)
            # Extract the period (e.g., 2限)
            period_match = re.search(r"(\d限)", line)
            if period_match:
                period = period_match.group(1)

        # Replace DTSTART and add DTEND with correct times
        if line.startswith("DTSTART;VALUE=DATE:") and period in period_times:
            date = line.split(":")[1]
            start_time, end_time = period_times[period]
            line = f"DTSTART;TZID=Asia/Tokyo:{date}T{start_time}"
            dtend = f"DTEND;TZID=Asia/Tokyo:{date}T{end_time}"
            updated_block.append(line)
            updated_block.append(dtend)
        else:
            updated_block.append(line)
    
    return updated_block

# Read the content from calendar.ics
with open('calendar.ics', 'r') as file:
    ics_content = file.read()

# Applying the update function
updated_ics = update_ics(ics_content)

# Write the updated content to result.ics
with open('result.ics', 'w') as file:
    file.write(updated_ics)
