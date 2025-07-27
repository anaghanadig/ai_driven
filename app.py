from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
import random
from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
from flask import request, render_template
from sqlalchemy import or_
import random
from flask_mail import Mail, Message
from flask import flash, render_template




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/aidriven'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'

db = SQLAlchemy(app)

# CompanyDetails Model
class CompanyDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-generated ID
    CompanyName = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=False)
    EmailID = db.Column(db.String(255), unique=True, nullable=False)
    Website = db.Column(db.String(255), nullable=False)
    ContactNumber = db.Column(db.String(15), nullable=False)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(50), nullable=False)


# CandidateDetails Model
class CandidateDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-generated ID
    FirstName = db.Column(db.String(50), nullable=False)
    MiddleName = db.Column(db.String(50))
    LastName = db.Column(db.String(50), nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    MobileNumber = db.Column(db.String(15), nullable=False)
    EmailID = db.Column(db.String(100), unique=True, nullable=False)
    TenthPercentage = db.Column(db.Float, nullable=False)
    TwelfthPercentage = db.Column(db.Float, nullable=False)
    Branch = db.Column(db.String(50), nullable=False)
    USNNumber = db.Column(db.String(20), unique=True, nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(100), nullable=False)
    

# Define the admin model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def _repr_(self):
        return f'<Contact {self.email}>'
    

class Jobs(db.Model):
    job_id = db.Column(db.Integer, primary_key=True, nullable=False)  # Primary key is defined here
    job_name = db.Column(db.String(100), nullable=False)
    job_location = db.Column(db.String(100), nullable=False)
    number_of_posts = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    company_address = db.Column(db.String(100), nullable=False)
    company_email_id = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Job {self.job_name} - {self.job_location}>"
    

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    branch = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)

class ApplyDetails(db.Model):
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_name = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    usn_number = db.Column(db.String(20), nullable=False)
    email_id = db.Column(db.String(100), nullable=False)
    mob = db.Column(db.String(15), nullable=False)

job_skills = {
    "Software Engineer": ["Python", "Java", "C++", "Algorithms", "Software Development"],
    "Data Analyst": ["SQL", "Data Visualization", "Excel", "Statistical Analysis"],
    "Project Manager": ["Team Leadership", "Scheduling", "Budget Management", "Communication"],
    "Machine Learning Engineer": ["Python", "Machine Learning", "Data Structures", "TensorFlow"],
     # Computer Science & Software Engineering (CSE)
    "Backend Developer": ["Java", "Spring Boot", "Microservices", "Databases"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React.js", "UI/UX Design"],
    "Data Scientist": ["Machine Learning", "Python", "Deep Learning", "Big Data", "Statistics"],
    "Machine Learning Engineer": ["TensorFlow", "Scikit-Learn", "AI Models", "Data Preprocessing"],
    "Cybersecurity Analyst": ["Network Security", "Cryptography", "Penetration Testing", "Ethical Hacking"],
    "Cloud Engineer": ["AWS", "Azure", "Google Cloud", "DevOps", "Kubernetes"],
    "Blockchain Developer": ["Ethereum", "Solidity", "Smart Contracts", "Hyperledger"],
    "Game Developer": ["Unity", "C#", "Game Physics", "3D Modeling", "Game AI"],
    "DevOps Engineer": ["CI/CD", "Docker", "Kubernetes", "Linux", "Cloud Deployment"],
     # Mechanical Engineering
    "Automobile Engineer": ["Vehicle Dynamics", "Engine Design", "Automotive Electronics"],
    "Manufacturing Engineer": ["CAD/CAM", "3D Printing", "Lean Manufacturing"],
    "Thermal Engineer": ["Heat Transfer", "Thermodynamics", "HVAC Systems"],

    # Civil Engineering
    "Structural Engineer": ["AutoCAD", "Reinforced Concrete Design", "Seismic Analysis"],
    "Construction Manager": ["Project Planning", "Construction Safety", "Cost Estimation"],
    "Geotechnical Engineer": ["Soil Mechanics", "Foundation Engineering", "Slope Stability"],

    # Electrical and Electronics Engineering (EEE)
    "Power Systems Engineer": ["Electrical Grid Systems", "Power Transmission", "Energy Management"],
    "Embedded Systems Engineer": ["Microcontrollers", "FPGA", "Real-Time Operating Systems"],
    "Renewable Energy Engineer": ["Solar Power", "Wind Energy", "Battery Storage Systems"],

    # Electronics and Communication Engineering (ECE)
    "VLSI Engineer": ["Chip Design", "Semiconductor Technology", "Verilog"],
    "Robotics Engineer": ["Embedded Systems", "Actuators & Sensors", "Robot Kinematics"],
    "Telecom Engineer": ["Wireless Communication", "5G Networks", "Antenna Design"],

    # Artificial Intelligence & Machine Learning (AIML)
    "AI Research Scientist": ["Deep Learning", "NLP", "Neural Networks"],
    "Computer Vision Engineer": ["OpenCV", "Image Processing", "Object Detection"],
    "AI Product Manager": ["AI Ethics", "Product Development", "User Experience"],

    # General Jobs (Non-Engineering)
    "Digital Marketing Specialist": ["SEO", "Social Media Marketing", "Google Ads"],
    "Human Resources Manager": ["Recruitment", "Employee Relations", "Performance Management"],
    "Finance Analyst": ["Financial Modeling", "Investment Analysis", "Accounting"],
    "Graphic Designer": ["Adobe Photoshop", "UI/UX Design", "Branding"],
    "Content Writer": ["Copywriting", "SEO Writing", "Blogging"],
     
    "AI Research Scientist": ["C++", "Deep Learning", "Neural Networks", "Computer Vision"],
    "Computer Vision Engineer": ["C++", "OpenCV", "Image Processing", "Object Detection"],
    "Autonomous Systems Engineer": ["C++", "ROS (Robot Operating System)", "SLAM (Simultaneous Localization & Mapping)"],

    # Cybersecurity & Networks
    "Cybersecurity Analyst": ["C++", "Network Security", "Cryptography", "Penetration Testing"],
    "Malware Analyst": ["C++", "Reverse Engineering", "Binary Analysis", "Cyber Forensics"],

    }


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/placed_students')
def placed_students():
    return render_template('placed_students.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')

@app.route('/company_page')
def company_page():
    return render_template('company_page.html')

@app.route('/candidate_page')
def candidate_page():
    return render_template('candidate_page.html')


@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    cs_count = CandidateDetails.query.filter_by(Branch='CSE').count()
    is_count = CandidateDetails.query.filter_by(Branch='ISE').count()
    eee_count = CandidateDetails.query.filter_by(Branch='EEE').count()
    ec_count = CandidateDetails.query.filter_by(Branch='ECE').count()
    me_count = CandidateDetails.query.filter_by(Branch='ME').count()
    civil_count = CandidateDetails.query.filter_by(Branch='civil').count()
    ei_count = CandidateDetails.query.filter_by(Branch='EI').count()
    company_count = CompanyDetails.query.count()
    job_count = Jobs.query.count()
    applications_count = ApplyDetails.query.count()  # Add this line
    
    return render_template('admin_dashboard.html', 
                         cs_count=cs_count, 
                         is_count=is_count, 
                         eee_count=eee_count, 
                         ec_count=ec_count, 
                         me_count=me_count,
                         civil_count=civil_count,
                         ei_count=ei_count,
                         company_count=company_count,
                         job_count=job_count,
                         applications_count=applications_count)  # Add this parameter

@app.route('/admin_companies')
def admin_companies():
    companies = CompanyDetails.query.all()
    return render_template('admin_companies.html', companies=companies)

@app.route('/admin_candidate')
def admin_candidate():
    candidates = CandidateDetails.query.all()
    return render_template('admin_candidate.html', candidates=candidates)

@app.route('/admin_search_by_branch', methods=['GET', 'POST'])
def admin_search_by_branch():
    candidates = []
    if request.method == 'POST':
       if request.method == 'POST':
        query = request.form['search'].strip()
        query = f"%{query}%"
        candidates = CandidateDetails.query.filter(
            (CandidateDetails.Branch.ilike(query)) |
            (CandidateDetails.FirstName.ilike(query)) |
            (CandidateDetails.LastName.ilike(query)) |
            (CandidateDetails.USNNumber.ilike(query)) |
            (CandidateDetails.EmailID.ilike(query))
        ).all()

    return render_template('admin_search_by_branch.html', candidates=candidates)
# report download
@app.route('/download_filtered_candidates')
def download_filtered_candidates():
    import csv
    from io import StringIO

    search_input = session.get('last_search', '')
    like_pattern = f"%{search_input}%"

    candidates = CandidateDetails.query.filter(
        (CandidateDetails.Branch.ilike(like_pattern)) |
        (CandidateDetails.FirstName.ilike(like_pattern)) |
        (CandidateDetails.MiddleName.ilike(like_pattern)) |
        (CandidateDetails.LastName.ilike(like_pattern)) |
        (CandidateDetails.USNNumber.ilike(like_pattern)) |
        (CandidateDetails.EmailID.ilike(like_pattern))
    ).all()

    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(["USN", "First Name", "Last Name", "Email", "Branch"])

    for c in candidates:
        cw.writerow([c.USNNumber, c.FirstName, c.LastName, c.EmailID, c.Branch])

    output = si.getvalue()
    return Response(output, mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=filtered_candidates_report.csv"})

# continue


@app.route('/admin_notifications', methods=['GET', 'POST'])
def admin_notifications():
    if request.method == 'POST':
        branch = request.form['branch']
        message = request.form['message']

        # Save the notification to the database
        new_notification = Notification(branch=branch, message=message)
        db.session.add(new_notification)
        db.session.commit()

        # Get the email addresses of candidates in the selected branch
        candidates = CandidateDetails.query.filter_by(Branch=branch).all()
        email_addresses = [candidate.EmailID for candidate in candidates]

        # Email configuration
        sender_email = "anughasha@gmail.com"  # Replace with your email
        app_password = "htwq yugr mfkd xiul"  # Replace with your app-specific password

        # Create the email subject and body
        subject = "Notification"
        body = f"""
        Hello,Students

        {message}

        Best regards,
        Placement Team MCE
        """

        try:
            # Establish SMTP connection
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, app_password)

                # Send the email to each candidate
                for recipient_email in email_addresses:
                    email_message = MIMEMultipart()  # Create a new message for each email
                    email_message["From"] = sender_email
                    email_message["To"] = recipient_email
                    email_message["Subject"] = subject
                    email_message.attach(MIMEText(body, "plain"))

                    # Send the email
                    server.sendmail(sender_email, recipient_email, email_message.as_string())
                    
                flash('Notification sent successfully to all candidates!', 'success')

        except smtplib.SMTPAuthenticationError:
            flash('Error: Authentication failed. Check your email and app password.', 'danger')
        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('admin_notifications.html')

@app.route('/company_home')
def company_home():
    return render_template('company_home.html')

@app.route('/company_dashboard')
def company_dashboard():
    cs_count = CandidateDetails.query.filter_by(Branch='CSE').count()
    is_count = CandidateDetails.query.filter_by(Branch='ISE').count()
    eee_count = CandidateDetails.query.filter_by(Branch='EEE').count()
    ec_count = CandidateDetails.query.filter_by(Branch='ECE').count()
    me_count = CandidateDetails.query.filter_by(Branch='ME').count()
    civil_count = CandidateDetails.query.filter_by(Branch='civil').count()
    ei_count = CandidateDetails.query.filter_by(Branch='EI').count()
    return render_template('company_dashboard.html', cs_count=cs_count, is_count=is_count, eee_count=eee_count, ec_count=ec_count,ei_count=ei_count,me_count=me_count,civil_count=civil_count)

@app.route('/company_add_or_delete_jobs', methods=['GET', 'POST'])
def company_add_or_delete_jobs():
    if request.method == 'POST':
        job_id = request.form['job_id']
        job_name = request.form['job_name']
        job_location = request.form['job_location']
        number_of_posts = request.form['number_of_posts']
        branch = request.form['branch']
        skills = request.form['sk']
        company_name = request.form['Company_name']
        company_address = request.form['Company_address']
        company_email_id = request.form['Company_email_id']


        try:
            # Create a new job entry
            new_job = Jobs(
            job_id = job_id,
            job_name=job_name,
            job_location=job_location,
            number_of_posts=number_of_posts,
            branch=branch,
            skills=skills,
            company_name=company_name,
            company_address=company_address,
            company_email_id=company_email_id
            )
            
            db.session.add(new_job)
            db.session.commit()

            flash('Job added successfully!', 'success')
            return redirect(url_for('company_add_or_delete_jobs'))
        except OperationalError:
            flash('Database connection error. Please try again later.', 'danger')
            return redirect(url_for('company_add_or_delete_jobs'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('company_add_or_delete_jobs'))

    return render_template('company_add_or_delete_jobs.html')

@app.route('/company_delete_jobs', methods=['GET', 'POST'])
def company_delete_jobs():
    if request.method == 'POST':
        job_id = request.form['job_id']
        job = Jobs.query.get(job_id)
        if job:
            db.session.delete(job)
            db.session.commit()
            flash('Job deleted successfully!', 'success')
        else:
            flash('Job not found!', 'danger')
    jobs = Jobs.query.all()
    return render_template('company_delete_jobs.html', jobs=jobs)


# search candidate company
@app.route('/company_candidates_search', methods=['GET', 'POST'])
def company_candidates_search():
    candidates = []
    search_term = ''

    if request.method == 'POST':
        search_term = request.form.get('search', '').strip()

        if search_term:
            candidates = CandidateDetails.query.filter(
                or_(
                    CandidateDetails.FirstName.ilike(f'%{search_term}%'),
                    CandidateDetails.LastName.ilike(f'%{search_term}%'),
                    CandidateDetails.EmailID.ilike(f'%{search_term}%'),
                    CandidateDetails.USNNumber.ilike(f'%{search_term}%'),
                    CandidateDetails.Branch.ilike(f'%{search_term}%'),
                    CandidateDetails.MobileNumber.ilike(f'%{search_term}%'),
                    CandidateDetails.Gender.ilike(f'%{search_term}%')
                    # Add or adjust fields based on your CandidateDetails model
                )
            ).all()

    return render_template('company_candidates_search.html', candidates=candidates)


@app.route('/candidate_home')
def candidate_home():
    return render_template('candidate_home.html')

@app.route('/candidate_dashboard')
def candidate_dashboard():
    cs_count = CandidateDetails.query.filter_by(Branch='CSE').count()
    eee_count = CandidateDetails.query.filter_by(Branch='EEE').count()
    ec_count = CandidateDetails.query.filter_by(Branch='ECE').count()
    is_count = CandidateDetails.query.filter_by(Branch='ISE').count()
    ec_count = CandidateDetails.query.filter_by(Branch='ECE').count()
    me_count = CandidateDetails.query.filter_by(Branch='ME').count()
    civil_count = CandidateDetails.query.filter_by(Branch='civil').count()
    ei_count = CandidateDetails.query.filter_by(Branch='EI').count()
    job_count = Jobs.query.count()
    company_count = CompanyDetails.query.count()
         
    branch = session['branch']
    USNNumber = session['username']
    EmailID = session['emailid']
    MobileNumber = session['mobilenumber']
    FirstName = session['firstname']
    skills = session['skills']
    
    # Get count of jobs applied by current user
    applied_jobs_count = ApplyDetails.query.filter_by(usn_number=USNNumber).count()
    
    # Query jobs matching the candidate's skills
    matching_jobs = Jobs.query.filter_by(skills=skills).all()
    
    return render_template('candidate_dashboard.html', 
                         cs_count=cs_count, 
                         is_count= is_count, 
                         eee_count=eee_count, 
                         ec_count=ec_count, 
                         me_count=me_count,
                         civil_count=civil_count,
                         ei_count=ei_count,
                         job_count=job_count, 
                         company_count=company_count,
                         branch=branch,
                         FirstName=FirstName,
                         USNNumber=USNNumber,
                         EmailID=EmailID,
                         MobileNumber=MobileNumber,
                         skills=skills,
                         applied_jobs_count=applied_jobs_count,
                         matching_jobs=matching_jobs)  # Pass matching jobs to the template

@app.route('/candidate_search_and_apply', methods=['GET', 'POST'])
def candidate_search_and_apply():
    jobs = Jobs.query.all()
    # Get current user's USN number from session
    usn_number = session.get('username')
    
    # Get all applications for this candidate
    applied_jobs = ApplyDetails.query.filter_by(usn_number=usn_number).all()
    # Create a set of job IDs that the candidate has already applied to
    applied_job_ids = {str(app.job_id) for app in applied_jobs}
    
    return render_template('candidate_search_and_apply.html', 
                         jobs=jobs, 
                         applied_job_ids=applied_job_ids)



@app.route('/candidate_search_and_apply1')
def candidate_search_and_apply1():
    # Get job details from URL parameters
    job_id = request.args.get('job_id')
    job_name = request.args.get('job_name')
    job_branch = request.args.get('job_branch')
    
    # Get candidate details from session
    firstname = session.get('firstname')
    usn_number = session.get('username')
    email_id = session.get('emailid')
    mobile_number = session.get('mobilenumber')
    
    try:
        # Create new application entry
        new_application = ApplyDetails(
            job_id=job_id,
            job_name=job_name,
            branch=job_branch,
            name=firstname,
            usn_number=usn_number,
            email_id=email_id,
            mob=mobile_number
        )
        
        # Save to database
        db.session.add(new_application)
        db.session.commit()
        
        flash('Job application submitted successfully!', 'success')
    except Exception as e:
        flash(f'Error submitting application: {str(e)}', 'danger')
    
    # Redirect back to job search page
    return redirect(url_for('candidate_search_and_apply'))

@app.route('/candidate_chatbot', methods=['GET', 'POST'])
def candidate_chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = chatbot_response(user_input)
        return render_template('candidate_chatbot.html', user_input=user_input, response=response)
    return render_template('candidate_chatbot.html')

@app.route('/candidate_match_my_skill_test')
def candidate_match_my_skill_test():
    # Convert skills string to list
    skills_string = session.get('skills', '').strip()
    user_skills = [skill.strip() for skill in skills_string.split(',')]

    # Get job recommendations
    recommended_jobs = recommend_jobs(user_skills)

    # Return both the original skills string and the processed skills list
    return render_template('candidate_match_my_skill_test.html',
                         skills_string=skills_string,
                         user_skills=user_skills,
                         recommended_jobs=recommended_jobs,
                         job_skills=job_skills)

def recommend_jobs(user_skills):
    recommendations = []
    
    # Check each job and compare the skills
    for job, skills in job_skills.items():
        # Calculate the number of matching skills
        matching_skills = set(user_skills) & set(skills)
        match_score = len(matching_skills)
        
        # If there is at least one matching skill, add the job to recommendations
        if match_score > 0:
            recommendations.append((job, match_score, matching_skills))
    
    # Sort recommendations by match score (in descending order)
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations

@app.route('/candidate_job_apply_history')
def candidate_job_apply_history():
    # Get current user's USN number from session
    usn_number = session.get('username')
    
    # Get all applications for this candidate
    applied_jobs = ApplyDetails.query.filter_by(usn_number=usn_number).all()
    
    return render_template('candidate_job_apply_history.html', applications=applied_jobs)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return render_template('login.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']

        # Create new Contact object
        new_contact = Contact(email=email, message=message)

        # Add contact to database
        db.session.add(new_contact)
        db.session.commit()

        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/forgot_password_candidate', methods=['GET', 'POST'])
def forgot_password_candidate():
    if request.method == 'POST':
        email = request.form['email']
        user = CandidateDetails.query.filter_by(EmailID=email).first()

        if user:
            new_password = generate_password()
            user.Password = new_password
            db.session.commit()

            # Email configuration
            sender_email = "anughasha@gmail.com"  # Replace with your email
            receiver_email = email  # Use the user's email
            password = "htwq yugr mfkd xiul"  # Replace with your app-specific password

            # Create the email
            subject = "Your New Password"
            body = f"""
            Hello,

            Your new password is: {new_password}
            Your Password has been reset ,Please note.

            Best regards,
            Your PlacemntMce
            """

            # Create a MIMEText object
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            # Attach the body to the email
            message.attach(MIMEText(body, "plain"))

            # Send the email
            try:
                # Connect to the SMTP server (for Gmail, use 'smtp.gmail.com' and port 587)
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    # Start TLS for security
                    server.starttls()

                    # Debugging: Print server responses
                    server.set_debuglevel(1)

                    # Login to the email account
                    server.login(sender_email, password)

                    # Send the email
                    server.sendmail(sender_email, receiver_email, message.as_string())

                print("Email sent successfully!")
            except smtplib.SMTPAuthenticationError:
                print("Error: Authentication failed. Check your email and password.")
            except Exception as e:
                print(f"Error: {e}")

            flash(f"Your new password has been sent to your email: {email}", 'info')
            return redirect(url_for('login'))
        else:
            flash('Email not found!', 'danger')
            
    return render_template('forgot_password_candidate.html')

@app.route('/forgot_password_company', methods=['GET', 'POST'])
def forgot_password_company():
    if request.method == 'POST':
        email = request.form['email']
        user = CompanyDetails.query.filter_by(EmailID=email).first()

        if user:
            new_password = generate_password()
            user.Password = new_password
            db.session.commit()

            # Email configuration
            sender_email = "anughasha@gmail.com"  # Replace with your email
            receiver_email = email  # Use the user's email
            password = "htwq yugr mfkd xiul"  # Replace with your app-specific password

            # Create the email
            subject = "Your New Password"
            body = f"""
            Hello,

            Your new password is: {new_password}
            Your Password has been reset ,Please note.

            Best regards,
            Your PlacementMce
            """

            # Create a MIMEText object
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            # Attach the body to the email
            message.attach(MIMEText(body, "plain"))

            # Send the email
            try:
                # Connect to the SMTP server (for Gmail, use 'smtp.gmail.com' and port 587)
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    # Start TLS for security
                    server.starttls()

                    # Debugging: Print server responses
                    server.set_debuglevel(1)

                    # Login to the email account
                    server.login(sender_email, password)

                    # Send the email
                    server.sendmail(sender_email, receiver_email, message.as_string())

                print("Email sent successfully!")
            except smtplib.SMTPAuthenticationError:
                print("Error: Authentication failed. Check your email and password.")
            except Exception as e:
                print(f"Error: {e}")

            flash(f"Your new password has been sent to your email: {email}", 'info')
            return redirect(url_for('login'))
        else:
            flash('Email not found!', 'danger')
            
    return render_template('forgot_password_company.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        username = request.form['username']
        password = request.form['password']

        if user_type == 'admin':
            user = Admin.query.filter_by(Username=username, Password=password).first()
            if user:
                session['username'] = user.Username
                return redirect(url_for('admin_home'))
        elif user_type == 'company':
            user = CompanyDetails.query.filter_by(Username=username, Password=password).first()
            if user:
                session['username'] = user.Username
                return redirect(url_for('company_home'))
        elif user_type == 'candidate':
            user = CandidateDetails.query.filter_by(USNNumber=username, Password=password).first()
            if user:
                session['username'] = user.USNNumber
                session['branch'] = user.Branch
                session['emailid'] = user.EmailID
                session['mobilenumber'] = user.MobileNumber
                session['firstname'] = user.FirstName
                session['skills'] = user.skills
                return redirect(url_for('candidate_home'))

        flash('Invalid username or password. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/company_registration', methods=['GET', 'POST'])
def company_registration():
    if request.method == 'POST':
        CompanyName = request.form['companyname']
        Address = request.form['address']
        EmailID = request.form['emailid']
        Website = request.form['website']
        ContactNumber = request.form['contactnumber']
        Username = request.form['username']
        Password = request.form['password']

        # Check if username or email already exists in the database
        existing_user = CompanyDetails.query.filter((CompanyDetails.Username == Username) | (CompanyDetails.EmailID == EmailID)).first()

        if existing_user:
            flash('Username or Email is already registered. Please choose a different one.', 'danger')
            return redirect(url_for('company_registration'))

        try:
            # Create a new company user
            new_user = CompanyDetails(
                CompanyName=CompanyName, 
                Address=Address, 
                EmailID=EmailID, 
                Website=Website, 
                ContactNumber=ContactNumber, 
                Username=Username, 
                Password=Password
            )
            
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except OperationalError:
            flash('Database connection error. Please try again later.', 'danger')
            return redirect(url_for('company_registration'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('company_registration'))

    return render_template('company_registration.html')


@app.route('/candidate_registration', methods=['GET', 'POST'])
def candidate_registration():
    if request.method == 'POST':
        FirstName = request.form['firstname']
        MiddleName = request.form['middlename']
        LastName = request.form['lastname']
        Gender = request.form['gender']
        MobileNumber = request.form['mobilenumber']
        EmailID = request.form['emailid']
        TenthPercentage = request.form['tenthpercentage']
        TwelfthPercentage = request.form['twelfthpercentage']
        Branch = request.form['branch']
        USNNumber = request.form['usnnumber']
        Password = request.form['password']
        Skills = request.form['Skills']

         # Check if username or email already exists in the database
        existing_user = CandidateDetails.query.filter((CandidateDetails.USNNumber == USNNumber) | (CandidateDetails.EmailID == EmailID)).first()

        if existing_user:
            flash('Username or Email is already registered. Please choose a different one.', 'danger')
            return redirect(url_for('candidate_registration'))

        try:
            # Create a new company user
            new_user = CandidateDetails(
                FirstName=FirstName,
                MiddleName=MiddleName,
                LastName=LastName,
                Gender=Gender,
                MobileNumber=MobileNumber,
                EmailID=EmailID,
                TenthPercentage=TenthPercentage,
                TwelfthPercentage=TwelfthPercentage,
                Branch=Branch,USNNumber=USNNumber,
                Password=Password,
                skills=Skills)
            
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except OperationalError:
            flash('Database connection error. Please try again later.', 'danger')
            return redirect(url_for('candidate_registration'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('candidate_registration'))

    return render_template('candidate_registration.html')


# A dictionary with simple question-response pairs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great, thank you!", "I'm just a bot, but I'm good!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "how to get placed": [
        "Prepare for technical interviews by mastering data structures and algorithms.",
        "Focus on problem-solving skills and participate in coding competitions.",
        "Strengthen at least one programming language like Java, Python, or C++.",
        "Practice mock interviews and behavioral questions.",
        "Work on projects and internships to gain hands-on experience."
    ],
    "which semester does placement start": [
        "Placements usually start in the 7th semester.",
        "Many companies visit colleges in the final year, around the 7th and 8th semesters."
    ],
    "what are important subjects for placements": [
        "Data Structures and Algorithms (DSA) is the most crucial.",
        "Object-Oriented Programming (OOPs), DBMS, OS, and Computer Networks are important.",
        "Aptitude and logical reasoning skills are also tested in many companies."
    ],
    "how to improve coding skills": [
        "Practice coding daily on platforms like LeetCode, CodeChef, and GeeksforGeeks.",
        "Solve at least 5-10 problems per week on different difficulty levels.",
        "Participate in hackathons and coding competitions.",
        "Study common coding patterns and problem-solving techniques."
    ],
    "what skills do companies look for": [
        "Strong programming and problem-solving skills.",
        "Good understanding of OOPs, DBMS, OS, and Networks.",
        "Strong aptitude and logical reasoning.",
        "Good communication and teamwork skills.",
        "Experience with real-world projects and internships."
    ],
    "how to prepare for HR interviews": [
        "Be confident and practice answering common HR questions.",
        "Know about the company and its values before the interview.",
        "Prepare answers for 'Tell me about yourself' and 'Why should we hire you?'.",
        "Be honest and give real-life examples to support your answers.",
        "Work on your communication skills and body language."
    ],
    "who is placement officer": [
        "B B Neelkantappa sir"
    ],
    "what is resume": [
        "A resume is a summary of your education, skills, and experience.",
        "It is used to apply for jobs and internships."
    ],
    "how to make a resume": [
        "Use online tools like Canva or Novoresume to create a simple resume.",
        "Include your name, contact info, education, skills, and projects.",
        "Keep it short and professional."
    ],
    "what is aptitude": [
        "Aptitude means your ability to solve problems quickly and logically.",
        "It is tested in most placement exams."
    ],
    "how to prepare for aptitude": [
        "Practice basic math, reasoning, and verbal questions regularly.",
        "Use apps like Pocket Aptitude or websites like IndiaBIX."
    ],
    "what are group discussions": [
        "Group Discussions (GD) are used to check your communication and thinking skills.",
        "You talk about a topic with other students and share your opinions."
    ],
    "how to prepare for GD": [
        "Read newspapers and stay updated with current topics.",
        "Practice speaking in front of a mirror or with friends.",
        "Listen to others and speak clearly with good points."
    ],
    "which languages should I learn": [
        "Start with C, C++ or Java for strong basics.",
        "Learn Python for data science and web development.",
        "JavaScript is good for web apps."
    ],
    "what is the role of projects": [
        "Projects show your practical skills and problem-solving ability.",
        "They help you stand out during placements."
    ],
    "companies visited 2025": [
        "Here’s a list of companies that visited our college for placements:",
        "Schneider, Bosch, Dish, Aarbee, Data Care, Ace Designers, Kalpataru, Shahi, Silo, IBM (Intern + FTE), Yokogawa, Toshiba, Devtools, Ascendion, Incresco, Difacto, Voya, Thoughtworks, MEIL, Cognizant, Toyota Kirloskar, TexasAI.",
    ]
}

company_names = [
    "toshiba", "benz", "tcs", "infosys", "tech mahindra",
    "ibm", "deloitte", "happiest minds", "toyota"
]

from flask import session

def chatbot_response(user_input):
    user_input = user_input.lower()
    branch = session.get('branch', 'CSE')  # fallback to CSE if not logged in

    for company in company_names:
        if company in user_input:
            predicted = predict_question(company, branch)
            return f"{company.title()} ({branch}) might ask: {predicted}"

    # Fallback
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I'm sorry, I don't understand that."
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.DataFrame({
    'Company': [
        'Toshiba', 'Benz', 'TCS', 'Infosys', 'Tech Mahindra',
        'IBM', 'Deloitte', 'Happiest Minds', 'Toyota', 'Toshiba', 'TCS', 'IBM', 'Infosys'
    ],
    'Branch': [
        'CSE', 'ME', 'CSE', 'CSE', 'ISE',
        'CSE', 'ECE', 'CSE', 'ECE', 'ISE', 'ISE', 'ECE', 'ISE'
    ],
    'Question': [
        'Explain memory management in C.',
        'What is ABS in cars?',
        'Difference between list and tuple in Python?',
        'What is OOPs concept?',
        'What is SDLC?',
        'Explain cloud computing basics.',
        'Tell me about a time you led a team.',
        'What is Agile methodology?',
        'Explain hybrid car technology.',
        'How does garbage collection work in Java?',
        'What are decorators in Python?',
        'Explain VLSI basics.',
        'What is the role of threading in Java?'
    ]
})

# Combine company + branch into features
data['Features'] = data['Company'].str.lower() + ' ' + data['Branch'].str.lower()
X = data['Features']
y = data['Question']

# Train TF-IDF and Naive Bayes model
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)
# here
y = data['Question']
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)

def predict_question(company, branch):
    input_text = f"{company.lower()} {branch.lower()}"
    X_input = vectorizer.transform([input_text])
    return model.predict(X_input)[0]

if __name__ == '__main__':
    app.run(debug=True)