import json

def create_midterm_review_questions():
    """Create additional quiz questions based on midterm review topics"""
    
    midterm_questions = [
        # ============ ENTERPRISE DEFINITIONS ============
        {
            "question_text": "What best describes an 'Enterprise' in the IT context?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Any small business with computers",
                "B": "A large-scale organization requiring complex, integrated systems with multiple users and stakeholders",
                "C": "Only Fortune 500 companies",
                "D": "Any company using cloud services"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "Which scenario would most favor choosing On-Premise over Cloud infrastructure?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Startup with limited IT budget",
                "B": "Company needing rapid scalability",
                "C": "Organization with strict regulatory requirements for data sovereignty",
                "D": "Small team with remote workers"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "What is the main difference between IaaS and SaaS?",
            "question_type": "multiple_choice",
            "options": {
                "A": "IaaS is more expensive than SaaS",
                "B": "IaaS provides infrastructure resources while SaaS provides complete applications",
                "C": "IaaS is for small companies, SaaS is for enterprises",
                "D": "There is no difference"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "Cloud infrastructure typically follows a Pay-As-You-Go operational expense model.",
            "question_type": "true_false",
            "correct_answer": True
        },
        {
            "question_text": "Which is an example of SaaS?",
            "question_type": "multiple_choice",
            "options": {
                "A": "AWS EC2",
                "B": "Azure Virtual Machines",
                "C": "Salesforce",
                "D": "Google Compute Engine"
            },
            "correct_answer": "C"
        },
        
        # ============ REQUIREMENTS CLASSIFICATION ============
        {
            "question_text": "'The system shall generate a monthly financial report' is an example of which type of requirement?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Non-Functional Requirement",
                "B": "Functional Requirement",
                "C": "Security Requirement",
                "D": "Performance Requirement"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "'The system shall be capable of handling 2 million concurrent users' is an example of which type of requirement?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Functional Requirement",
                "B": "Non-Functional Requirement",
                "C": "Business Requirement",
                "D": "User Requirement"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "'The system web pages shall be displayed on Chrome, Firefox and Safari' is what type of requirement?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Functional Requirement",
                "B": "Security Requirement",
                "C": "Non-Functional Requirement (Compatibility)",
                "D": "Data Requirement"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "Non-Functional Requirements define WHAT a system does, while Functional Requirements define HOW WELL it does it.",
            "question_type": "true_false",
            "correct_answer": False
        },
        
        # ============ STAKEHOLDER QUESTIONS ============
        {
            "question_text": "Which of the following would NOT typically be considered a stakeholder in an enterprise software project?",
            "question_type": "multiple_choice",
            "options": {
                "A": "IT Operations Team",
                "B": "End Users",
                "C": "Competitors",
                "D": "Project Manager"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "In a tool assessment for a knowledge base system, which aspect would the IT Department be MOST concerned with?",
            "question_type": "multiple_choice",
            "options": {
                "A": "User interface design",
                "B": "Security features and on-premise deployment capability",
                "C": "Cost per user",
                "D": "Number of emojis supported"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "When assessing a knowledge base tool, developers would be most interested in which features?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Licensing costs and budget",
                "B": "Search capabilities and code snippet support",
                "C": "Hardware requirements",
                "D": "Backup procedures"
            },
            "correct_answer": "B"
        },
        
        # ============ DEVOPS PRACTICES ============
        {
            "question_text": "What are the three primary practice areas of DevOps?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Planning, Coding, Testing",
                "B": "Build, Test, Deploy",
                "C": "Continuous Delivery, Infrastructure Automation, Site Reliability Engineering",
                "D": "Agile, Scrum, Kanban"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "A CI pipeline should ideally be triggered:",
            "question_type": "multiple_choice",
            "options": {
                "A": "Once a week",
                "B": "On every commit to source control",
                "C": "Only before releases",
                "D": "Manually by the build master"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "Which should NOT be stored in your source code repository?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Jenkinsfile",
                "B": "Database schemas",
                "C": "Compiled binaries",
                "D": "Test scripts"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "Database schemas and migration scripts should be stored in your source code repository.",
            "question_type": "true_false",
            "correct_answer": True
        },
        
        # ============ JENKINS PIPELINE SPECIFICS ============
        {
            "question_text": "Where should the Jenkinsfile (pipeline definition) be stored?",
            "question_type": "multiple_choice",
            "options": {
                "A": "On the Jenkins server only",
                "B": "In source control with the code",
                "C": "In a separate documentation repository",
                "D": "On a network file share"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "What is the primary advantage of using Jenkins Shared Libraries?",
            "question_type": "multiple_choice",
            "options": {
                "A": "They make pipelines run faster",
                "B": "They enable code reuse and reduce duplication",
                "C": "They eliminate the need for testing",
                "D": "They automatically fix bugs"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "In a Jenkinsfile, what does the 'agent' directive specify?",
            "question_type": "multiple_choice",
            "options": {
                "A": "The person responsible for the build",
                "B": "Where the pipeline or stage will execute",
                "C": "The version control system",
                "D": "The test framework to use"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "A 'stage' in a Jenkins pipeline represents:",
            "question_type": "multiple_choice",
            "options": {
                "A": "A development environment",
                "B": "A distinct phase like Build, Test, or Deploy",
                "C": "A Jenkins plugin",
                "D": "A user role"
            },
            "correct_answer": "B"
        },
        
        # ============ SOFTWARE UPDATES & PRODUCTION ============
        {
            "question_text": "What is the Production environment?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Where developers write code",
                "B": "The testing environment",
                "C": "The live environment where end users access the software",
                "D": "The staging environment"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "Before updating Production, which is NOT a recommended planning activity?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Create a rollback plan",
                "B": "Test changes in staging",
                "C": "Skip notifications to avoid panic",
                "D": "Backup current state"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "When is the best time to perform Production updates that require downtime?",
            "question_type": "multiple_choice",
            "options": {
                "A": "During peak business hours",
                "B": "During low-traffic periods outside business hours",
                "C": "Randomly to test system resilience",
                "D": "Every morning at 9 AM"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "If something goes wrong during a Production update, the first action should be:",
            "question_type": "multiple_choice",
            "options": {
                "A": "Try to fix it in Production",
                "B": "Execute the rollback plan immediately",
                "C": "Blame the developers",
                "D": "Wait and see if it fixes itself"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "A rollback plan should be created AFTER attempting a Production update.",
            "question_type": "true_false",
            "correct_answer": False
        },
        
        # ============ ENVIRONMENT IMPROVEMENTS ============
        {
            "question_text": "Which is a security improvement for an Enterprise Development Environment?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Removing all passwords",
                "B": "Implementing role-based access control (RBAC)",
                "C": "Allowing anonymous access",
                "D": "Disabling all logging"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "From a maintainability perspective, which improvement would be most valuable?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Manual configuration of each server",
                "B": "Infrastructure as Code",
                "C": "Avoiding documentation",
                "D": "Hard-coding configurations"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "Which would be a usability improvement for developers using the Enterprise Environment?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Requiring separate passwords for each tool",
                "B": "Single Sign-On (SSO) integration",
                "C": "Command-line only interfaces",
                "D": "Removing all documentation"
            },
            "correct_answer": "B"
        },
        {
            "question_text": "Multi-factor authentication is primarily which type of improvement?",
            "question_type": "multiple_choice",
            "options": {
                "A": "Usability",
                "B": "Performance",
                "C": "Security",
                "D": "Cost reduction"
            },
            "correct_answer": "C"
        },
        {
            "question_text": "Containerization with Docker primarily helps with:",
            "question_type": "multiple_choice",
            "options": {
                "A": "Security only",
                "B": "Maintainability and consistency",
                "C": "Reducing costs only",
                "D": "User interface design"
            },
            "correct_answer": "B"
        }
    ]
    
    return midterm_questions

def add_to_existing_quiz(new_questions, existing_file="quiz_questions.json"):
    """Add new questions to existing quiz file"""
    
    # Load existing questions
    try:
        with open(existing_file, 'r') as f:
            existing_questions = json.load(f)
        print(f"✅ Loaded {len(existing_questions)} existing questions")
    except FileNotFoundError:
        existing_questions = []
        print("⚠️ No existing file found, creating new one")
    
    # Add new questions
    existing_questions.extend(new_questions)
    
    # Save combined questions
    with open(existing_file, 'w') as f:
        json.dump(existing_questions, f, indent=2)
    
    return len(existing_questions)

def main():
    print("="*70)
    print("MIDTERM REVIEW QUESTIONS GENERATOR")
    print("="*70)
    
    # Create midterm review questions
    new_questions = create_midterm_review_questions()
    print(f"\n📝 Created {len(new_questions)} new midterm review questions")
    
    # Topics covered
    print("\n📚 Topics covered in new questions:")
    print("  • Enterprise definitions (Cloud vs On-Premise, IaaS vs SaaS)")
    print("  • Requirements classification (Functional vs Non-Functional)")
    print("  • Stakeholder identification and perspectives")
    print("  • DevOps practices and CI pipelines")
    print("  • Jenkins pipeline concepts")
    print("  • Production updates and rollback procedures")
    print("  • Environment improvements (Security, Maintainability, Usability)")
    
    # Ask if user wants to add to existing quiz
    choice = input("\n💾 Add these to your existing quiz? (y/n): ").lower()
    
    if choice == 'y':
        total = add_to_existing_quiz(new_questions)
        print(f"\n✅ Success! Your quiz now has {total} total questions")
        print("\n🚀 To practice:")
        print("   python quiz_app.py")
    else:
        # Save as separate file
        filename = "midterm_review_quiz.json"
        with open(filename, 'w') as f:
            json.dump(new_questions, f, indent=2)
        print(f"\n📁 Saved as separate file: {filename}")
        print("\n To use: Run quiz_app.py and enter 'midterm_review_quiz' as custom filename")
    
    print("\n💡 Study Tips:")
    print("  • Focus on understanding concepts, not memorization")
    print("  • Practice identifying requirement types")
    print("  • Know when to use Cloud vs On-Premise")
    print("  • Understand the DevOps pipeline flow")
    print("  • Review stakeholder perspectives for tool assessments")

if __name__ == "__main__":
    main()