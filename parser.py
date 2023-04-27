def parse_data(section):
    lines = section.text.split("\n")
    parsed_lines = []
    links = section.find_elements(By.TAG_NAME, "a")
    link_map = {link.text: link.get_attribute('href') for link in links}
    for line in lines:
        if line in link_map:
            line += f" ({link_map[line]})"
        parsed_lines.append(line)
    return "\n".join(parsed_lines)
