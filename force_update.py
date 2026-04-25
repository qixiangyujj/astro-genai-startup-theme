import os
import re

def force_update_content(directory):
    if not os.path.exists(directory):
        return
        
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".astro", ".ts", ".js", ".json", ".md", ".tsx")):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. 強制替換公司名稱 (忽略大小寫，涵蓋之前改錯的所有版本)
                updated = re.sub(r'GenAI|Polyhedron\s?Tech', 'Polyhedrontech', content, flags=re.IGNORECASE)
                
                # 2. 強制替換主標題
                updated = re.sub(r'Build the Future with AI|AI-Powered Enterprise Solutions', 'Your Ultimate Family AI Solution', updated, flags=re.IGNORECASE)
                
                # 3. 強制替換副標題/描述
                updated = re.sub(r'Automate your workflow.*?for modern teams\.|Enterprise Cloud & AI Architecture', 'Smart Family NAS & Memory Management.', updated, flags=re.IGNORECASE)
                
                if content != updated:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated)
                    print(f"✅ 強制更新成功: {filepath}")

force_update_content('src')
force_update_content('public')
print("替換完成！請運行 npm run dev 檢查。")
