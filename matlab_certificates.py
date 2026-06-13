"""
Martha Heita - MATLAB Certificates & Achievement Hub
Computer Programming I - Semester 1, 2026
"""

# MATLAB Certificates completed by Martha Heita
# All certificates from MathWorks Learning Center

MATLAB_CERTIFICATES = [
    {
        "id": 1,
        "title": "MATLAB Fundamentals",
        "description": "Core concepts and basic syntax",
        "date_completed": "2026-05-15",
        "url": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=6da7c3e8-d5d4-4fff-bfc5-b15af346cd80",
        "skills": ["Variables", "Data Types", "Arrays", "Basic Operations"]
    },
    {
        "id": 2,
        "title": "Matrix & Array Operations",
        "description": "Working with matrices and multidimensional arrays",
        "date_completed": "2026-05-20",
        "url": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=f3b1987c-2f0a-4636-9632-2b534bc43ec0",
        "skills": ["Matrix Creation", "Indexing", "Linear Algebra", "Element-wise Operations"]
    },
    {
        "id": 3,
        "title": "Programming Constructs",
        "description": "Control flow, loops, and conditional statements",
        "date_completed": "2026-05-25",
        "url": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=28b37ba8-1fcb-48b2-bcd0-a93aa0c2a7a3",
        "skills": ["if/else", "for/while loops", "Switch statements", "Logical operators"]
    },
    {
        "id": 4,
        "title": "Functions & Scripts",
        "description": "Writing and organizing reusable code",
        "date_completed": "2026-06-01",
        "url": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=6561d974-aeaa-4c93-a8fd-6ae5ad4eafe5",
        "skills": ["Function Definition", "Input/Output", "Scope", "Error Handling"]
    },
    {
        "id": 5,
        "title": "Data Visualization",
        "description": "Creating plots and visual representations",
        "date_completed": "2026-06-05",
        "url": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=229e1482-1b85-4e2a-b938-e6cb221edb8f",
        "skills": ["2D/3D Plotting", "Customization", "Subplots", "Annotation"]
    },
    {
        "id": 6,
        "title": "File I/O Operations",
        "description": "Reading and writing data files",
        "date_completed": "2026-06-10",
        "url": "https://matlabacademy.mathworks.com/progress/share/certificate.html?id=7c020a63-33bc-4f24-a0b9-09ddbe219b20",
        "skills": ["File Reading", "CSV/Excel", "Data Export", "File Formats"]
    }
]

# Remaining 2 certificates to complete for full 8/8
REMAINING_CERTIFICATES = [
    {
        "id": 7,
        "title": "String Operations",
        "description": "Text manipulation and string processing",
        "status": "In Progress",
        "estimated_completion": "June 2026"
    },
    {
        "id": 8,
        "title": "Advanced Debugging",
        "description": "Debugging techniques and troubleshooting",
        "status": "Not Started",
        "estimated_completion": "Late June 2026"
    }
]

def get_certificate_progress():
    """Calculate certificate completion percentage"""
    completed = len(MATLAB_CERTIFICATES)
    total = completed + len(REMAINING_CERTIFICATES)
    return (completed / total) * 100

def get_all_certificates():
    """Get all certificate information"""
    return {
        "completed": MATLAB_CERTIFICATES,
        "remaining": REMAINING_CERTIFICATES,
        "progress": get_certificate_progress(),
        "total_completed": len(MATLAB_CERTIFICATES),
        "total_required": len(MATLAB_CERTIFICATES) + len(REMAINING_CERTIFICATES)
    }

if __name__ == "__main__":
    certs = get_all_certificates()
    print(f"MATLAB Certificates Completed: {certs['total_completed']}/{certs['total_required']}")
    print(f"Progress: {certs['progress']:.1f}%")
    print("\nCompleted Courses:")
    for cert in certs['completed']:
        print(f"  ✓ {cert['title']} - {cert['date_completed']}")
