# ENTERPRISE SYSTEMS INTEGRATION - MIDTERM REVIEW ANSWERS

## DEFINITIONS

### What's an Enterprise?
An enterprise is a large-scale organization or business that typically operates across multiple departments, locations, or business units. In IT context, it refers to organizations that require complex, integrated systems to support their operations, with multiple users, teams, and stakeholders.

### Cloud vs On-Premise Differences
**Cloud:**
- Hosted and maintained by third-party providers
- Pay-as-you-go operational expense model
- Accessible from anywhere with internet
- Provider handles maintenance and updates
- Scalable on demand

**On-Premise:**
- Hosted on organization's own infrastructure
- Capital expense with upfront investment
- Controlled entirely by your organization
- You handle all maintenance and updates
- Fixed capacity unless you buy more hardware

**When to favor Cloud:**
- Small company with limited IT resources
- Need rapid scalability
- Want to minimize upfront costs
- Distributed teams needing remote access
- Don't have sensitive regulatory requirements

**When to favor On-Premise:**
- Strict security/compliance requirements
- Handling highly sensitive data (trade secrets, classified info)
- Need complete control over infrastructure
- Have existing IT infrastructure and expertise
- Regulatory requirements mandate local data storage

### IaaS vs SaaS Differences
**IaaS (Infrastructure as a Service):**
- Provides virtual computing resources (servers, storage, networking)
- You manage the OS, applications, and data
- Examples: AWS EC2, Azure VMs, Google Compute Engine

**SaaS (Software as a Service):**
- Complete applications delivered over the internet
- Provider manages everything including the application
- Examples: Salesforce, Office 365, Google Workspace

**When to favor IaaS:**
- Need custom configurations or specific OS requirements
- Want control over the software stack
- Have complex integration requirements
- Need to run legacy applications

**When to favor SaaS:**
- Want ready-to-use applications
- Limited IT resources
- Standard business processes
- Don't need heavy customization

## REQUIREMENTS

### Functional Requirements
- Define what a system should DO
- Describe specific functions, features, and behaviors
- Specify the relationship between inputs and outputs
- Examples: "System shall process credit card payments", "System shall generate monthly reports"

### Non-Functional Requirements
- Define constraints on HOW the system operates
- Describe quality attributes and performance criteria
- Also called "ilities" or System Quality Attributes
- Also called Architecturally Significant Requirements
- Examples: Performance, Security, Usability, Scalability, Maintainability

### Difference Between Functional and Non-Functional
- Functional = WHAT the system does (features/functions)
- Non-Functional = HOW WELL it does it (quality/constraints)

### Requirements Examples Analysis
From the provided examples:
1. **Functional** - Generate monthly report (what it does)
2. **Functional** - Display latest report (what it does)
3. **Functional** - Download as PDF (what it does)
4. **Non-Functional** - Browser compatibility (constraint/quality)
5. **Non-Functional** - Restore within one hour (performance requirement)

## STAKEHOLDERS

### Definition
A stakeholder is anyone who has an interest in or will be affected by the realization of a system, project, or tool. They may influence or be influenced by the project's outcome.

### Examples of Stakeholders
- **Project Manager** - Oversees project delivery
- **Development Team** - Builds the system
- **IT Operations Team** - Maintains infrastructure
- **Test Team** - Ensures quality
- **End Users/Customers** - Use the system
- **Management/Executives** - Provide funding and strategic direction
- **Support Team** - Helps users
- **Security Team** - Ensures compliance
- **HR** (for HR systems) - Domain experts

## TOOL ASSESSMENTS

### Knowledge Base Tool Assessment Perspectives

**Team Managers would assess:**
- Cost and licensing model
- Reporting and analytics capabilities
- User access control and permissions
- Integration with project management tools
- Ability to track contributions and usage
- Scalability for team growth

**Software Developers would assess:**
- Ease of use and user interface
- Search capabilities
- Code snippet support and formatting
- Version control for documents
- API availability for integration
- Collaboration features (comments, real-time editing)
- Mobile accessibility
- Performance and response time

**IT Department would assess:**
- On-premise deployment capability
- System requirements (hardware/software)
- Security features and encryption
- Backup and disaster recovery
- Integration with existing infrastructure (Active Directory, SSO)
- Maintenance requirements
- Update and patching procedures
- Database options
- High availability options

## DEVOPS

### Three Primary Practice Areas
1. **Continuous Delivery** - Automated build, test, and deployment pipelines
2. **Infrastructure Automation** - Infrastructure as Code, configuration management
3. **Site Reliability Engineering** - Monitoring, orchestration, designing for operability

### What a CI Pipeline Does
- Automatically builds code when changes are committed
- Runs automated tests to catch issues early
- Provides fast feedback to developers
- Ensures code integration happens frequently
- Reduces integration conflicts

### Characteristics of Good CI Pipeline
- **Fast** - Quick feedback loop
- **Automated** - Minimal manual intervention
- **Reliable** - Consistent and repeatable
- **Visible** - Clear status and results
- **Comprehensive** - Includes build, test, and analysis
- **Triggered automatically** - On every code change

### Source Code Repository Contents
**Should Include:**
- Source code files
- Build scripts and configurations
- Test scripts and test data
- Database schemas and migration scripts
- Documentation
- Configuration files
- Jenkinsfile/Pipeline definitions

**Should NOT Include:**
- Compiled binaries
- Temporary files
- Large media files (use LFS if needed)
- Passwords or secrets
- Personal IDE settings
- Generated documentation

## PIPELINES - JENKINSFILE

### Main Jenkinsfile Keywords
- **pipeline** - Defines the entire pipeline block
- **agent** - Specifies where pipeline executes
- **stages** - Groups related stages
- **stage** - Defines distinct phase (Build, Test, Deploy)
- **steps** - Individual tasks within a stage
- **when** - Conditional execution
- **post** - Actions after stage/pipeline completion

### Shared Library Definition
Consists of three components:
1. **Name** - Library identifier
2. **Version** - Specific version or branch
3. **Source Code Retrieval Method** - How Jenkins fetches it (Git URL)

### Advantages of Shared Libraries
- **Code Reuse** - DRY principle
- **Centralized maintenance** - Update once, use everywhere
- **Standardization** - Consistent practices across projects
- **Reduced duplication** - Less copy-paste
- **Easier updates** - Change library, all pipelines benefit

### Pipeline Storage and Execution
- **Storage**: Jenkinsfile stored in source control with code
- **Execution Frequency**: Ideally on every commit to source control

## SOFTWARE UPDATES

### Production Environment
The live environment where end users access the software. It's the final stage where the application serves its intended purpose for actual customers/users.

### Update Frequency
- Depends on organization and criticality
- Can range from multiple times daily (continuous deployment) to monthly/quarterly
- Balance between new features and stability

### Planning Activities Before Update
- Review and test changes in staging
- Create rollback plan
- Schedule maintenance window
- Notify stakeholders and users
- Backup current state
- Document update procedures
- Verify dependencies

### If Something Goes Wrong
- Execute rollback plan immediately
- Restore from backup
- Communicate with stakeholders
- Document what went wrong
- Conduct post-mortem analysis
- Fix issues before reattempting

### When to Do Updates
- During low-traffic periods
- Outside business hours (nights/weekends)
- Scheduled maintenance windows
- Agreed upon with stakeholders
- When minimal users are affected

## ENTERPRISE DEVELOPMENT ENVIRONMENT IMPROVEMENTS

### Security Improvements
- Implement role-based access control (RBAC)
- Enable SSL/TLS for all communications
- Regular security patching
- Audit logging for all actions
- Secrets management (vault)
- Network segmentation
- Multi-factor authentication
- Regular security scans

### Maintainability Improvements
- Infrastructure as Code
- Automated backups
- Monitoring and alerting
- Documentation and runbooks
- Containerization (Docker)
- Configuration management
- Automated testing
- Version control for everything

### Usability Improvements
- Single Sign-On (SSO)
- Intuitive user interfaces
- Comprehensive documentation
- Training materials
- Quick start guides
- Responsive design
- Search functionality
- Keyboard shortcuts
- Customizable dashboards

---

# QUIZ QUESTIONS TO ADD

Based on the midterm review, here are additional quiz questions to add to your study materials: