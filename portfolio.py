"""
Martha Heita - Individual Web Portfolio
Flet Python Framework
Computer Programming I - Semester 1, 2026
"""

import flet as ft
import json
from datetime import datetime
from typing import List, Dict

class PortfolioApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Martha Heita - Computer Programming I Portfolio"
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.theme_mode = ft.ThemeMode.LIGHT
        
        # Navigation state
        self.current_view = "dashboard"
        
        # Portfolio data
        self.portfolio_data = self.load_portfolio_data()
        
        self.build_ui()
    
    def load_portfolio_data(self) -> Dict:
        """Load portfolio content"""
        return {
            "name": "Martha Heita",
            "course": "Computer Programming I",
            "semester": "1, 2026",
            "github": "https://github.com/marthandilimengungo-dotcom",
            "matlab_certificates": 6,
            "total_commits": 8,
            "project_timeline": [
                {
                    "week": 1,
                    "date": "June 1-7, 2026",
                    "contribution": "Project Setup & Architecture Design",
                    "details": "Initialized repository structure, configured Flet development environment, and designed portfolio architecture."
                },
                {
                    "week": 2,
                    "date": "June 8-14, 2026",
                    "contribution": "UI Framework & Navigation Implementation",
                    "details": "Built responsive navigation system, created theme configuration, and implemented core portfolio sections."
                },
            ],
            "github_evidence": {
                "recent_commits": [
                    {
                        "hash": "9c6dc37faf8907e83b7c1539b02ba242e7f747ca",
                        "message": "Merge pull request #1 - Implement individual web portfolio",
                        "date": "2026-06-13T13:04:21Z",
                        "url": "https://github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio/commit/9c6dc37faf8907e83b7c1539b02ba242e7f747ca"
                    },
                    {
                        "hash": "6520dc4855cef533fed3005a70bbd5806201207a",
                        "message": "feat: Add to-do list and digital clock applications with full documentation",
                        "date": "2026-06-13T12:56:57Z",
                        "url": "https://github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio/commit/6520dc4855cef533fed3005a70bbd5806201207a"
                    }
                ],
                "pull_requests": [
                    {
                        "number": 1,
                        "title": "Implement individual web portfolio for Martha Heita",
                        "status": "merged",
                        "url": "https://github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio/pull/1"
                    }
                ]
            },
            "blog_posts": [
                {
                    "title": "Data Structures & Algorithms: From Theory to Practice",
                    "date": "June 2026",
                    "excerpt": "Understanding how data structures and algorithms form the backbone of efficient programming.",
                    "content": """
## Data Structures & Algorithms: From Theory to Practice

### Introduction
Data structures and algorithms are fundamental concepts in computer science. They enable us to solve complex problems efficiently and write scalable code. This post explores key concepts and their practical applications.

### 1. Time Complexity Analysis

When analyzing algorithm efficiency, we use Big O notation to describe the worst-case time complexity.

**Formal Definition:**
Let f(n) and g(n) be functions. We say f(n) = O(g(n)) if there exist positive constants c and n₀ such that:

    f(n) ≤ c·g(n) for all n ≥ n₀

**Common Complexities (from fastest to slowest):**
- O(1) - Constant time
- O(log n) - Logarithmic
- O(n) - Linear
- O(n log n) - Linearithmic
- O(n²) - Quadratic
- O(2ⁿ) - Exponential
- O(n!) - Factorial

### 2. Arrays vs Linked Lists

**Arrays:**
- Access: O(1) - Direct indexing
- Search: O(n) - Linear search, O(log n) - Binary search
- Insertion/Deletion: O(n) - May require shifting elements
- Space: Contiguous memory block

**Linked Lists:**
- Access: O(n) - Must traverse from head
- Search: O(n) - Sequential search required
- Insertion/Deletion: O(1) - If position is known
- Space: Non-contiguous, scattered memory

### 3. Sorting Algorithms Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|-----------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

### 4. Practical Example: Binary Search

**Problem:** Find a target value in a sorted array.

**Algorithm:**
```
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
```

**Complexity:** O(log n)

**Why it's better than linear search:**
- Linear search: 1,000,000 elements → 1,000,000 comparisons
- Binary search: 1,000,000 elements → 20 comparisons

### 5. Real-World Applications

1. **Web Search Engines:** Use sophisticated algorithms to rank and retrieve results
2. **Social Media:** Graph algorithms for friend recommendations
3. **Navigation Apps:** Dijkstra's algorithm for shortest path
4. **Databases:** B-trees for efficient indexing and retrieval
5. **Compression:** Huffman coding algorithm reduces file sizes

### Conclusion

Mastering data structures and algorithms is crucial for writing efficient, scalable code. By understanding their trade-offs and complexities, you can make informed decisions when designing solutions to real-world problems.
""",
                    "video_url": "https://www.youtube.com/embed/09PWDjwFtL0"
                }
            ]
        }
    
    def build_ui(self):
        """Build main UI structure"""
        self.page.clean()
        
        # Create navigation rail
        nav_rail = self.create_navigation_rail()
        
        # Create main content area
        main_content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("", size=1)  # Placeholder for dynamic content
                ],
                expand=True
            ),
            expand=True
        )
        
        # Layout: Navigation + Content
        layout = ft.Row(
            controls=[nav_rail, ft.VerticalDivider(width=1), main_content],
            expand=True
        )
        
        self.page.add(layout)
        self.main_content = main_content
        
        # Show dashboard by default
        self.show_dashboard()
    
    def create_navigation_rail(self) -> ft.NavigationRail:
        """Create side navigation"""
        return ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.DASHBOARD,
                    label="Dashboard"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.CALENDAR_MONTH,
                    label="Timeline"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SCHOOL,
                    label="MATLAB Hub"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.ARTICLE,
                    label="Blog"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.CODE,
                    label="GitHub"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.INFO,
                    label="About"
                ),
            ],
            on_change=self.on_nav_change,
        )
    
    def on_nav_change(self, e):
        """Handle navigation changes"""
        index = e.control.selected_index
        views = ["dashboard", "timeline", "matlab", "blog", "github", "about"]
        self.current_view = views[index]
        
        if self.current_view == "dashboard":
            self.show_dashboard()
        elif self.current_view == "timeline":
            self.show_timeline()
        elif self.current_view == "matlab":
            self.show_matlab()
        elif self.current_view == "blog":
            self.show_blog()
        elif self.current_view == "github":
            self.show_github()
        elif self.current_view == "about":
            self.show_about()
    
    def show_dashboard(self):
        """Dashboard view"""
        data = self.portfolio_data
        
        content = ft.Column(
            controls=[
                ft.Text("Martha Heita - Portfolio Dashboard", size=32, weight="bold"),
                ft.Divider(),
                
                ft.Row(
                    controls=[
                        self.create_stat_card("Total Commits", str(data["total_commits"]), ft.icons.GIT_COMMIT),
                        self.create_stat_card("MATLAB Courses", f"{data['matlab_certificates']}/8", ft.icons.SCHOOL),
                        self.create_stat_card("Blog Posts", "1", ft.icons.ARTICLE),
                        self.create_stat_card("PRs Merged", "1", ft.icons.MERGE_TYPE),
                    ],
                    wrap=True
                ),
                
                ft.Text("Course Information", size=20, weight="bold"),
                ft.Text(f"Course: {data['course']}", size=14),
                ft.Text(f"Semester: {data['semester']}", size=14),
                ft.Text(f"Portfolio CA Weight: 15%", size=14),
                
                ft.Text("Assessment Breakdown", size=18, weight="bold"),
                self.create_assessment_breakdown(),
                
                ft.ElevatedButton(
                    text="View Full Portfolio →",
                    icon=ft.icons.ARROW_FORWARD,
                    on_click=lambda e: self.show_github()
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        
        self.main_content.content = content
        self.page.update()
    
    def create_stat_card(self, title: str, value: str, icon: str) -> ft.Card:
        """Create a statistic card"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(name=icon, size=40, color=ft.colors.PRIMARY),
                        ft.Text(value, size=24, weight="bold"),
                        ft.Text(title, size=12, color=ft.colors.GREY_700),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                padding=20,
                alignment=ft.alignment.center
            ),
            elevation=2
        )
    
    def create_assessment_breakdown(self) -> ft.Column:
        """Create assessment breakdown"""
        assessments = [
            ("Flet Implementation", 30),
            ("GitHub Evidence", 25),
            ("Blog & Video", 25),
            ("MATLAB Courses", 20),
        ]
        
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(name, size=12, width=150),
                        ft.ProgressBar(value=marks/100, width=200),
                        ft.Text(f"{marks}%", size=12, width=50),
                    ]
                ) for name, marks in assessments
            ],
            spacing=10
        )
    
    def show_timeline(self):
        """Project timeline view"""
        timeline_items = []
        
        for item in self.portfolio_data["project_timeline"]:
            timeline_items.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(f"Week {item['week']}: {item['date']}", weight="bold", size=14),
                                ft.Text(item['contribution'], size=12, weight="w500"),
                                ft.Text(item['details'], size=11, color=ft.colors.GREY_700),
                            ],
                            spacing=5
                        ),
                        padding=15
                    )
                )
            )
        
        content = ft.Column(
            controls=[
                ft.Text("Project Timeline", size=32, weight="bold"),
                ft.Divider(),
                ft.Text("Weekly Contributions to Group Project", size=14),
                ft.Column(controls=timeline_items, spacing=10),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        
        self.main_content.content = content
        self.page.update()
    
    def show_matlab(self):
        """MATLAB Achievement Hub"""
        content = ft.Column(
            controls=[
                ft.Text("MATLAB Achievement Hub", size=32, weight="bold"),
                ft.Divider(),
                ft.ProgressRing(
                    value=self.portfolio_data["matlab_certificates"] / 8,
                    width=100,
                    height=100,
                ),
                ft.Text(
                    f"{self.portfolio_data['matlab_certificates']}/8 Courses Completed",
                    size=18,
                    weight="bold"
                ),
                ft.Text(
                    "MathWorks Learning Center Courses",
                    size=12,
                    color=ft.colors.GREY_700
                ),
                ft.Divider(),
                ft.Text("Completed Courses:", size=14, weight="bold"),
                ft.Column(
                    controls=[
                        ft.Row(controls=[
                            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                            ft.Text("MATLAB Fundamentals")
                        ]),
                        ft.Row(controls=[
                            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                            ft.Text("Matrix & Array Operations")
                        ]),
                        ft.Row(controls=[
                            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                            ft.Text("Programming Constructs")
                        ]),
                        ft.Row(controls=[
                            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                            ft.Text("Functions & Scripts")
                        ]),
                        ft.Row(controls=[
                            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                            ft.Text("Data Visualization")
                        ]),
                        ft.Row(controls=[
                            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                            ft.Text("File I/O Operations")
                        ]),
                    ],
                    spacing=8
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        
        self.main_content.content = content
        self.page.update()
    
    def show_blog(self):
        """Blog view"""
        blog_post = self.portfolio_data["blog_posts"][0]
        
        content = ft.Column(
            controls=[
                ft.Text("Technical Blog", size=32, weight="bold"),
                ft.Divider(),
                ft.Text("Confidence in Concepts", size=14, color=ft.colors.GREY_700),
                
                ft.Text(blog_post["title"], size=24, weight="bold"),
                ft.Text(blog_post["date"], size=12, color=ft.colors.GREY_700),
                ft.Divider(),
                
                ft.Markdown(
                    blog_post["content"],
                    selectable=True,
                    extension_set=ft.markdown.ExtensionSet.GITHUB_WEB
                ),
                
                ft.Divider(),
                ft.Text("Embedded Video Resource", size=14, weight="bold"),
                ft.Text("YouTube: Data Structures & Algorithms Tutorial", size=12),
                ft.TextButton(
                    text="Watch on YouTube →",
                    icon=ft.icons.VIDEO_LIBRARY,
                    on_click=lambda e: self.open_link(blog_post["video_url"])
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        
        self.main_content.content = content
        self.page.update()
    
    def show_github(self):
        """GitHub Evidence view"""
        evidence = self.portfolio_data["github_evidence"]
        
        commits_list = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(commit["message"], weight="bold", size=12),
                            ft.Text(commit["hash"][:8], size=10, color=ft.colors.GREY_700),
                            ft.Text(commit["date"], size=10, color=ft.colors.GREY_700),
                            ft.TextButton(
                                text="View Commit →",
                                on_click=lambda e, url=commit["url"]: self.open_link(url)
                            ),
                        ],
                        spacing=5
                    ),
                    padding=10
                )
            ) for commit in evidence["recent_commits"]
        ]
        
        content = ft.Column(
            controls=[
                ft.Text("GitHub Evidence & Documentation", size=32, weight="bold"),
                ft.Divider(),
                
                ft.Text("Repository", size=18, weight="bold"),
                ft.TextButton(
                    text="github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio",
                    on_click=lambda e: self.open_link("https://github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio")
                ),
                
                ft.Divider(),
                ft.Text(f"Recent Commits ({len(evidence['recent_commits'])})", size=16, weight="bold"),
                ft.Column(controls=commits_list, spacing=8),
                
                ft.Divider(),
                ft.Text(f"Pull Requests ({len(evidence['pull_requests'])})", size=16, weight="bold"),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("#1 - Implement individual web portfolio for Martha Heita", weight="bold"),
                                ft.Badge(text="MERGED", bgcolor=ft.colors.GREEN),
                                ft.TextButton(
                                    text="View PR →",
                                    on_click=lambda e: self.open_link(evidence["pull_requests"][0]["url"])
                                ),
                            ],
                            spacing=5
                        ),
                        padding=10
                    )
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        
        self.main_content.content = content
        self.page.update()
    
    def show_about(self):
        """About view"""
        content = ft.Column(
            controls=[
                ft.Text("About This Portfolio", size=32, weight="bold"),
                ft.Divider(),
                
                ft.Text("Martha Heita", size=24, weight="bold"),
                ft.Text("Computer Programming I Student | Semester 1, 2026", size=14, color=ft.colors.GREY_700),
                
                ft.Divider(),
                ft.Text("Portfolio Overview", size=16, weight="bold"),
                ft.Text(
                    "This portfolio serves as comprehensive evidence of individual contributions to the Computer Programming I course. "
                    "It demonstrates proficiency in:\n"
                    "• Python programming with the Flet framework\n"
                    "• Version control and collaborative development\n"
                    "• Technical communication and documentation\n"
                    "• MATLAB fundamentals and scientific computing",
                    size=12
                ),
                
                ft.Divider(),
                ft.Text("Assessment Components", size=16, weight="bold"),
                
                ft.ExpansionTile(
                    title="Flet Implementation (30%)",
                    subtitle="Code structure and deployment",
                    children=[
                        ft.Text("This portfolio is built entirely with Flet Python Framework, demonstrating "
                               "responsive design, navigation patterns, and web deployment capabilities.", size=11)
                    ]
                ),
                
                ft.ExpansionTile(
                    title="GitHub Evidence (25%)",
                    subtitle="Commit history and PR documentation",
                    children=[
                        ft.Text("Complete commit history and pull request logs demonstrating individual "
                               "contributions and code review processes.", size=11)
                    ]
                ),
                
                ft.ExpansionTile(
                    title="Technical Blog & Video (25%)",
                    subtitle="Confidence in concepts",
                    children=[
                        ft.Text("Written technical explanations with mathematical notation and embedded "
                               "video resources for core programming concepts.", size=11)
                    ]
                ),
                
                ft.ExpansionTile(
                    title="MATLAB Achievements (20%)",
                    subtitle="Verification of 8 MathWorks certificates",
                    children=[
                        ft.Text("Completion verification for MathWorks Learning Center courses covering "
                               "MATLAB fundamentals and advanced concepts.", size=11)
                    ]
                ),
                
                ft.Divider(),
                ft.Text("Contact & Links", size=16, weight="bold"),
                ft.Row(
                    controls=[
                        ft.TextButton(
                            text="GitHub",
                            icon=ft.icons.CODE,
                            on_click=lambda e: self.open_link("https://github.com/marthandilimengungo-dotcom")
                        ),
                        ft.TextButton(
                            text="Portfolio Repo",
                            icon=ft.icons.FOLDER,
                            on_click=lambda e: self.open_link("https://github.com/marthandilimengungo-dotcom/MarthaHeitaPortfolio")
                        ),
                    ],
                    spacing=10
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
        
        self.main_content.content = content
        self.page.update()
    
    def open_link(self, url: str):
        """Open external link"""
        import webbrowser
        webbrowser.open(url)


def main(page: ft.Page):
    app = PortfolioApp(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
