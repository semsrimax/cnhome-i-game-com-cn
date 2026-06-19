import json
from datetime import datetime
from typing import Dict, List, Optional

SITE_DATA = {
    "title": "爱游戏平台",
    "url": "https://cnhome-i-game.com.cn",
    "description": "专注于提供高质量数字娱乐体验的综合游戏平台，涵盖多种类型的在线游戏与社交互动功能。",
    "keywords": ["爱游戏", "在线游戏", "数字娱乐", "游戏平台"],
    "tags": ["游戏", "娱乐", "互动", "社区"],
    "language": "zh-CN",
    "category": "游戏门户",
    "features": [
        "多人在线对战",
        "每日任务系统",
        "成就徽章收集",
        "实时排行榜",
        "好友社交网络"
    ],
    "contact": {
        "email": "support@cnhome-i-game.com.cn",
        "type": "客户支持"
    }
}

class SiteSummaryGenerator:
    """生成网站结构化摘要的工具类"""
    
    def __init__(self, site_info: Dict[str, any] = None):
        self.site = site_info or SITE_DATA
        self._validate()
    
    def _validate(self):
        """验证基础数据完整性"""
        required = ["title", "url", "description"]
        for field in required:
            if field not in self.site:
                raise ValueError(f"缺少必要字段: {field}")
    
    def get_basic_info(self) -> Dict[str, str]:
        """提取基本信息"""
        return {
            "站点名称": self.site["title"],
            "网址": self.site["url"],
            "简介": self.site["description"],
            "语言": self.site.get("language", "未知"),
            "类别": self.site.get("category", "未分类")
        }
    
    def format_tags(self) -> str:
        """格式化标签列表"""
        tags = self.site.get("tags", [])
        return "、".join(tags) if tags else "无标签"
    
    def format_keywords(self) -> str:
        """格式化关键词列表"""
        kws = self.site.get("keywords", [])
        return "、".join(kws) if kws else "无关键词"
    
    def generate_summary_text(self) -> str:
        """生成纯文本摘要"""
        lines = []
        lines.append("=" * 50)
        lines.append(f"  站点摘要报告")
        lines.append(f"  生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("=" * 50)
        lines.append("")
        
        info = self.get_basic_info()
        for key, value in info.items():
            lines.append(f"  {key}: {value}")
        
        lines.append(f"  关键词: {self.format_keywords()}")
        lines.append(f"  标签:   {self.format_tags()}")
        
        features = self.site.get("features", [])
        if features:
            lines.append("")
            lines.append("  特色功能:")
            for i, feat in enumerate(features, 1):
                lines.append(f"    {i}. {feat}")
        
        contact = self.site.get("contact")
        if contact:
            lines.append("")
            lines.append(f"  联系方式: {contact.get('email', '未提供')} ({contact.get('type', '未知')})")
        
        lines.append("")
        lines.append("=" * 50)
        return "\n".join(lines)
    
    def generate_html_summary(self) -> str:
        """生成 HTML 格式的摘要"""
        info = self.get_basic_info()
        features = self.site.get("features", [])
        contact = self.site.get("contact")
        
        html_parts = []
        html_parts.append('<div class="site-summary">')
        html_parts.append(f'  <h2>{self._escape_html(info["站点名称"])}</h2>')
        html_parts.append(f'  <p><strong>网址:</strong> <a href="{self._escape_html(info["网址"])}">{self._escape_html(info["网址"])}</a></p>')
        html_parts.append(f'  <p><strong>简介:</strong> {self._escape_html(info["简介"])}</p>')
        html_parts.append(f'  <p><strong>语言:</strong> {self._escape_html(info["语言"])} | <strong>类别:</strong> {self._escape_html(info["类别"])}</p>')
        html_parts.append(f'  <p><strong>关键词:</strong> {self._escape_html(self.format_keywords())}</p>')
        html_parts.append(f'  <p><strong>标签:</strong> {self._escape_html(self.format_tags())}</p>')
        
        if features:
            html_parts.append('  <h3>特色功能</h3>')
            html_parts.append('  <ul>')
            for feat in features:
                html_parts.append(f'    <li>{self._escape_html(feat)}</li>')
            html_parts.append('  </ul>')
        
        if contact:
            html_parts.append(f'  <p><strong>联系:</strong> {self._escape_html(contact.get("email", ""))}</p>')
        
        html_parts.append('</div>')
        return "\n".join(html_parts)
    
    def to_json(self, indent: int = 2) -> str:
        """将站点数据转为 JSON 字符串"""
        output = {
            "summary": {
                "generated_at": datetime.now().isoformat(),
                "title": self.site["title"],
                "url": self.site["url"],
                "description": self.site["description"],
                "keywords": self.site.get("keywords", []),
                "tags": self.site.get("tags", []),
                "features": self.site.get("features", []),
                "contact": self.site.get("contact")
            }
        }
        return json.dumps(output, ensure_ascii=False, indent=indent)
    
    @staticmethod
    def _escape_html(text: str) -> str:
        """转义 HTML 特殊字符"""
        replacements = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;"
        }
        for char, escaped in replacements.items():
            text = text.replace(char, escaped)
        return text
    
    def print_summary(self):
        """直接打印文本摘要"""
        print(self.generate_summary_text())


def main():
    """主函数：演示站点摘要生成"""
    print("=== 站点摘要生成演示 ===\n")
    
    generator = SiteSummaryGenerator()
    
    print("【文本摘要】")
    generator.print_summary()
    
    print("\n【HTML 摘要预览】")
    print(generator.generate_html_summary())
    
    print("\n【JSON 数据】")
    print(generator.to_json())
    
    print("\n演示完成。")


if __name__ == "__main__":
    main()