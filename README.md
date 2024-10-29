# Calendar Script

This project contains scripts to process and update `.ics` calendar files. The main functionality includes translating course names from Japanese to English and updating event timestamps based on predefined periods.

## Files

- `scholarship.py`: Contains functions related to event creation and signup period parsing.
- `script.py`: Contains the main logic for processing and updating `.ics` files.

## Functions

### `scholarship.py`

- `create_event(name, start_date, end_date, all_day=True)`: Creates an all-day event.
- `parse_signup_period(month, signup_period)`: Parses the signup period and returns the start and end dates.

### `script.py`

- `process_event_block(event_block)`: Processes a block of event data, translating course names and updating timestamps.
- `update_ics(file_content)`: Reads the content of an `.ics` file, processes each event block, and returns the updated content.

## Usage

1. **Read the content from `calendar.ics`:**
  ```python
  with open('calendar.ics', 'r') as file:
    ics_content = file.read()
  ```

2. **Apply the update function:**
  ```python
  updated_ics = update_ics(ics_content)
  ```

3. **Write the updated content to `result.ics`:**
  ```python
  with open('result.ics', 'w') as file:
    file.write(updated_ics)
  ```

## Course Translation

The script translates the following Japanese course names to English:

- 自然科学総論Ⅰ: General Natural Sciences I
- 放射線防護学特論: Topics in Radiation Protection
- 数理計画概論: Introduction to Mathematical Programming
- 機能性表面特論: Advanced Functional Surfaces
- 宇宙探査ロボティクス特論: Space Exploration Robotics
- ネットワーク・セキュリティ特論: Advanced Networks and Security
- 移動情報ネットワーク特論: Advanced Mobile Information Networks
- ソフトウエア構成論特論: Software Construction
- 産業スペシャリスト育成特論: Training Course for Industrial Specialists
- 技術・社会システム工学総論: Science, Technology and Society, General
- コミュニケーション支援特論: Assistive Technology for Communication
- ビジネス英語: Business English
- 地盤防災論: Geotechnical Disaster Management
- 集中日本語０ G: Intensive Japanese 0
- 西洋言語概説: Lecture on Western Languages

## Period Times

The script updates event timestamps based on the following periods:

- 1限: 08:30 - 10:00
- 2限: 10:15 - 11:45
- 3限: 12:55 - 14:25
- 4限: 14:40 - 16:10
- 5限: 16:25 - 17:55

## License

This project is licensed under the MIT License.