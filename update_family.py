import os

def update_content(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".astro", ".ts", ".js", ".json", ".md")):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 將企業標語替換為家庭 AI 標語
                updated = content.replace("AI-Powered Enterprise Solutions", "Your Ultimate Family AI Solution")
                updated = updated.replace("Enterprise Cloud & AI Architecture", "Smart Family NAS & Memory Management")
                
                if content != updated:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated)
                    print(f"✅ 定位已更新: {filepath}")

update_content('src')
update_content('public')
