import os
import re

files_to_update = [
    "frontend/src/components/BottomNav.jsx",
    "frontend/src/components/SuccessModal.jsx",
    "frontend/src/pages/CashierPage.jsx",
    "frontend/src/pages/ExpensesPage.jsx",
    "frontend/src/pages/HistoryPage.jsx",
    "frontend/src/pages/LoginPage.jsx",
    "frontend/src/pages/MorePage.jsx",
    "frontend/src/pages/ProductsPage.jsx",
    "frontend/src/pages/ReportsPage.jsx",
    "frontend/src/pages/UsersPage.jsx",
]

emoji_to_lucide = {
    "🏪": "<Store size={20} />",
    "📋": "<ClipboardList size={20} />",
    "📊": "<BarChart2 size={20} />",
    "☰": "<Menu size={20} />",
    "💰": "<Wallet size={24} />",
    "📦": "<Package size={24} />",
    "👥": "<Users size={24} />",
    "💳": "<CreditCard size={24} />",
    "💵": "<Banknote size={24} />",
    "📉": "<TrendingDown size={24} />",
    "📈": "<TrendingUp size={24} />",
    "🍞": "<Croissant size={24} />",
    "🚪": "<LogOut size={20} />",
    "🗑️": "<Trash2 size={16} />",
    "✏️": "<Edit2 size={16} />",
    "👑": "<Crown size={16} />",
    "👤": "<User size={16} />",
    "✖": "<X size={20} />",
    "❌": "<X size={20} />"
}

imports = {
    "frontend/src/components/BottomNav.jsx": "import { Store, ClipboardList, BarChart2, Menu } from 'lucide-react';\n",
    "frontend/src/components/SuccessModal.jsx": "import { Croissant } from 'lucide-react';\n",
    "frontend/src/pages/CashierPage.jsx": "import { Croissant, CreditCard, Banknote } from 'lucide-react';\n",
    "frontend/src/pages/ExpensesPage.jsx": "import { TrendingDown, Trash2 } from 'lucide-react';\n",
    "frontend/src/pages/HistoryPage.jsx": "import { ClipboardList } from 'lucide-react';\n",
    "frontend/src/pages/LoginPage.jsx": "import { Croissant } from 'lucide-react';\n",
    "frontend/src/pages/MorePage.jsx": "import { Store, ClipboardList, BarChart2, Wallet, Package, Users, CreditCard, Banknote, TrendingDown, TrendingUp, Croissant, LogOut } from 'lucide-react';\n",
    "frontend/src/pages/ProductsPage.jsx": "import { Package, Croissant, Edit2, Trash2 } from 'lucide-react';\n",
    "frontend/src/pages/ReportsPage.jsx": "import { Wallet, CreditCard, Banknote, Package, Croissant, TrendingDown, TrendingUp } from 'lucide-react';\n",
    "frontend/src/pages/UsersPage.jsx": "import { Crown, User, Trash2 } from 'lucide-react';\n",
}

for filepath in files_to_update:
    path = os.path.join(r"c:\Users\Acer\Desktop\non", filepath)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add import
    if "lucide-react" not in content:
        # Find first import or top of file
        first_import = re.search(r"^import\s+.*", content, flags=re.MULTILINE)
        if first_import:
            content = content[:first_import.start()] + imports.get(filepath, "") + content[first_import.start():]
        else:
            content = imports.get(filepath, "") + content

    # Replace Emojis
    # We must be careful not to replace emojis inside strings if they are used as plain text, 
    # but in JSX they are mostly strings.
    # Wait, in React `<div className="icon">🍞</div>` will become `<div className="icon"><Croissant size={24} /></div>`
    # But `{ icon: '🏪', label: 'Касса' }` will become `{ icon: <Store size={20} />, label: 'Касса' }`
    
    # We will do some specific regexes for string wrapped ones vs non-string wrapped
    
    for emoji, tag in emoji_to_lucide.items():
        # Case 1: wrapped in quotes e.g. '🏪' -> <Store size={20} />
        content = re.sub(rf"['\"]{emoji}['\"]", tag, content)
        # Case 2: raw emoji in JSX e.g. >🏪< -> ><Store size={20} /><
        content = content.replace(emoji, tag)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Replacement complete")
