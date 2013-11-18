# Import modules
from pyPdf import PdfFileReader
import re
from os import listdir

# Set up any OCR here

# Set up stopwords here

# Path of all resumes in an array here
resumes = listdir("Analytics/Intro to Analytics/MSiA 400 Resumes/Resume Packet UTenn/")

# Sets empty arrays for pdfs and pngs
resumes_pdf = []
resumes_png = []

# sort resume function here
# Just testing now
for r in resumes:
  resumes_pdf.append(r)

# Declares an array for text
resumes_text = []

# Extracts text from pdfs and pushes it into text array
for r in range(1, len(resumes_pdf)):
  print "Analytics/Intro to Analytics/MSiA 400 Resumes/Resume Packet UTenn/" + resumes_pdf[r]
  resume = PdfFileReader(file("Analytics/Intro to Analytics/MSiA 400 Resumes/Resume Packet UTenn/" + resumes_pdf[r], "rb"))
  num_pages = resume.getNumPages()
  text = ""
  for i in range(0, num_pages):
    text = text + resume.getPage(i).extractText()
  resumes_text.append(text)

# Extract text from png

# Declares an array for all results
all_results = []

# Instantiates an empty dictionary
# A dictionary is a key: value pair
# So it will store the keywords and their counts
keywords = {}

# Write keyword search method here

# Write method to loop through resumes and perform keyword search

# Sort keywords

# Print keywords to file

# Some (non-python) dictionaries for several categories
universities = ["Harvard University", "Stanford University", "University of California, Berkeley", "Massachusetts Institute of Technology", "University of Cambridge", "California Institute of Technology", "Princeton University", "Columbia University", "University of Chicago", "University of Oxford", "Yale University", "University of California, Los Angeles", "Cornell University", "University of California, San Diego", "University of Pennsylvania", "University of Washington", "The Johns Hopkins University", "University of California, San Francisco", "University of Wisconsin - Madison", "Swiss Federal Institute of Technology Zurich", "The University of Tokyo", "University College London", "University of Michigan - Ann Arbor", "The Imperial College of Science, Technology and Medicine", "University of Illinois at Urbana-Champaign", "Kyoto University", "New York University", "University of Toronto", "University of Minnesota, Twin Cities", "Northwestern University", "Duke University", "Washington University in St. Louis", "University of Colorado at Boulder", "Rockefeller University", "University of California, Santa Barbara", "The University of Texas at Austin", "Pierre and Marie Curie University - Paris 6", "University of Maryland, College Park", "University of Paris Sud (Paris 11)", "University of British Columbia", "The University of Manchester", "University of Copenhagen", "University of North Carolina at Chapel Hill", "Karolinska Institute", "University of California, Irvine", "The University of Texas Southwestern Medical Center at Dallas", "University of California, Davis", "University of Southern California", "Vanderbilt University", "Technical University Munich", "The University of Edinburgh", "Carnegie Mellon University", "Utrecht University", "Pennsylvania State University - University Park", "University of Heidelberg", "University of Melbourne", "Purdue University - West Lafayette", "McGill University", "The Hebrew University of Jerusalem", "University of Zurich", "Rutgers, The State University of New Jersey - New Brunswick", "University of Munich", "University of Pittsburgh", "University of Bristol", "The Ohio State University - Columbus", "The Australian National University", "Brown University", "King's College London", "University of Geneva", "University of Oslo", "Ecole Normale Superieure - Paris", "University of Florida", "Uppsala University", "Leiden University", "Boston University", "University of Helsinki", "Technion-Israel Institute of Technology", "University of Arizona", "Arizona State University - Tempe", "Moscow State University", "Aarhus University", "Stockholm University", "University of Basel", "University of Nottingham", "Ghent University", "Indiana University Bloomington", "Osaka University", "The University of Queensland", "University of Utah", "University of Rochester", "The University of Western Australia", "McMaster University", "Michigan State University", "Rice University", "University of Groningen", "Weizmann Institute of Science", "University of Strasbourg", "University of Sydney", "Case Western Reserve University", "University of Freiburg", "Baylor College of Medicine", "Catholic University of Leuven", "Catholic University of Louvain", "Emory University", "Georgia Institute of Technology", "Hokkaido University", "Joseph Fourier University (Grenoble 1)", "London School of Economics and Political Science", "Lund University", "Mayo Medical School", "Monash University", "Nagoya University", "National Taiwan University", "National University of Singapore", "Oregon State University", "Radboud University Nijmegen", "Seoul National University", "Swiss Federal Institute of Technology of Lausanne", "Tel Aviv University", "Texas A&M University - College Station", "The University of Georgia", "The University of Sheffield", "The University of Texas M. D. Anderson Cancer Center", "Tohoku University", "Tokyo Institute of Technology", "Tufts University", "University Libre Bruxelles", "University of Alberta", "University of Amsterdam", "University of Birmingham", "University of Bonn", "University of California, Riverside", "University of California, Santa Cruz", "University of Frankfurt", "University of Goettingen", "University of Iowa", "University of Liverpool", "University of Massachusetts Amherst", "University of Massachusetts Medical School - Worcester", "University of Montreal", "University of Muenster", "University of New South Wales", "University of Paris Diderot (Paris 7)", "University of Pisa", "University of Roma - La Sapienza", "University of Sao Paulo", "University of Sussex", "University of Virginia", "University of Wageningen", "VU University Amsterdam", "Aix Marseille University", "Cardiff University", "Colorado State University", "Dartmouth College", "Erasmus University", "Florida State University", "Fudan University", "George Mason University", "Iowa State University", "King Saud University", "Kyushu University", "Mount Sinai School of Medicine", "National Autonomous University of Mexico", "North Carolina State University - Raleigh", "Oregon Health and Science University", "Peking University", "Shanghai Jiao Tong University", "State University of New York at Stony Brook", "Technical University of Denmark", "The Chinese University of Hong Kong", "The University of Glasgow", "The University of Texas Health Science Center at Houston", "Tsinghua University", "University of Bern", "University of Buenos Aires", "University of Delaware", "University of Gothenburg", "University of Hamburg", "University of Hawaii at Manoa", "University of Illinois at Chicago", "University of Kiel", "University of Koeln", "University of Leeds", "University of Mainz", "University of Maryland, Baltimore", "University of Miami", "University of Milan", "University of Padua", "University of Paris Descartes (Paris 5)", "University of Southampton", "University of Tennessee - Knoxville", "University of Tsukuba", "University of Tuebingen", "University of Vienna", "University of Warwick", "University of Waterloo", "University of Wuerzburg", "Virginia Commonwealth University", "Virginia Polytechnic Institute and State University", "Zhejiang University", "Autonomous University of Barcelona", "Autonomous University of Madrid", "Brandeis University", "Charles University in Prague", "Claude Bernard University Lyon 1", "Complutense University of Madrid", "Dalhousie University", "Delft University of Technology", "Dresden University of Technology", "Ecole Normale Superieure - Lyon", "Ecole Polytechnique", "Karlsruhe Institute of Technology (KIT)", "King Abdulaziz University", "Kobe University", "Korea Advanced Institute of Science and Technology", "Laval University", "Louisiana State University - Baton Rouge", "Macquarie University", "Medical University of Vienna", "Nanjing University", "Nanyang Technological University", "National Tsing Hua University", "Newcastle University", "Norwegian University of Science and Technology", "Paul Sabatier University (Toulouse 3)", "Polytechnic Institute of Milan", "Queen Mary, U. of London", "Queen's University", "Rensselaer Polytechnic Institute", "Royal Institute of Technology", "RWTH Aachen University", "Scuola Normale Superiore - Pisa", "Simon Fraser University", "State University of New York at Buffalo", "Sun Yat-sen University", "Sungkyunkwan University", "Swedish University of Agricultural Sciences", "Technical University of Berlin", "The George Washington University", "The Hong Kong University of Science and Technology", "The University of Adelaide", "The University of Alabama at Birmingham", "The University of Auckland", "The University of Calgary", "The University of Connecticut - Storrs", "The University of Dundee", "The University of Hong Kong", "The University of New Mexico - Albuquerque", "The University of Western Ontario", "Thomas Jefferson University", "Trinity College Dublin", "Umea University", "University of Aberdeen", "University of Antwerp", "University of Barcelona", "University of Bergen", "University of Bologna", "University of Bordeaux", "University of Cape Town", "University of Central Florida", "University of Cincinnati", "University of Colorado at Denver", "University of Duesseldorf", "University of Durham", "University of East Anglia", "University of Erlangen-Nuremberg", "University of Exeter", "University of Florence", "University of Guelph", "University of Houston", "University of Innsbruck", "University of Kansas - Lawrence", "University of Kentucky", "University of Lausanne", "University of Leicester", "University of Leipzig", "University of Liege", "University of Lorraine", "University of Maastricht", "University of Marburg", "University of Medicine and Dentistry New Jersey", "University of Missouri - Columbia", "University of Montpellier 2", "University of Nebraska - Lincoln", "University of Notre Dame", "University of Oregon", "University of Otago", "University of Ottawa", "University of Paris Dauphine (Paris 9)", "University of Saskatchewan", "University of Science and Technology of China", "University of South Florida", "University of Southern Denmark", "University of St Andrews", "University of Stuttgart", "University of Turin", "University of York", "Washington State University - Pullman", "Yeshiva University", "Yonsei University", "Aristotle University of Thessaloniki", "Bar-Ilan University", "Beijing Normal University", "Ben-Gurion University of the Negev", "Brigham Young University", "Chalmers University of Technology", "Chang Gung University", "China Agricultural University", "City University of Hong Kong", "City University of New York City College", "Clemson University", "Eindhoven University of Technology", "Eotvos Lorand University", "Federal University of Minas Gerais", "Federal University of Rio de Janeiro", "Flinders University", "Georgetown University", "Griffith University", "Hanyang University", "Harbin Institute of Technology", "Hiroshima University", "Huazhong University of Science and Technology", "Indian Institute of Science", "Industrial Physics and Chemistry Higher Educational Institution - Paris", "Jagiellonian University", "James Cook University", "Jilin University", "Kansas State University", "Keio University", "King Fahd University of Petroleum & Minerals", "Korea University", "Lancaster University", "Linkoping University", "Medical University of South Carolina", "National and Kapodistrian University of Athens", "National Cheng Kung University", "National Chiao Tung University", "Northeastern University", "Okayama University", "Pohang University of Science and Technology", "Polytechnic University of Valencia", "Queen's University Belfast", "Saint Louis University", "Saint Petersburg State University", "San Diego State University", "Sao Paulo State University", "Shandong University", "Sichuan University", "State University of Campinas", "State University of New York at Albany", "State University of New York Health Science Center at Brooklyn", "Swinburne University of Technology", "Syracuse University", "Technical University Darmstadt", "Temple University", "The Hong Kong Polytechnic University", "The University of Montana - Missoula", "The University of Reading", "The University of Texas at Dallas", "The University of Texas Health Science Center at San Antonio", "Tokyo Medical and Dental University", "Tulane University", "University College Cork", "University College Dublin", "University of Bath", "University of Belgrade", "University of Bochum", "University of Genova", "University of Giessen", "University of Granada", "University of Halle-Wittenberg", "University of Konstanz", "University of Lisbon", "University of Manitoba", "University of Naples Federico II", "University of Newcastle", "University of Nice Sophia Antipolis", "University of Oklahoma - Norman", "University of Oulu", "University of Perugia", "University of Pompeu Fabra", "University of Porto", "University of Regensburg", "University of Rhode Island", "University of South Carolina - Columbia", "University of Tasmania", "University of the Witwatersrand", "University of Turku", "University of Twente", "University of Ulm", "University of Valencia", "University of Vermont", "University of Victoria", "University of Warsaw", "University of Wollongong", "Vrije University Brussel", "Wake Forest University", "Waseda University", "Wayne State University", "Xian Jiao Tong University", "Auburn University", "Beihang University", "Boston College", "Cairo University", "Carleton University", "Catholic University of Chile", "Catholic University of Korea", "Catholic University of the Sacred Heart", "Central South University", "China Medical University", "Concordia University", "Curtin University of Technology", "Dalian University of Technology", "Drexel University", "Ecole National Superieure Mines - Paris", "Federal University of Rio Grande do Sul", "Hannover Medical School", "Indiana University-Purdue University at Indianapolis", "Istanbul University", "Kanazawa University", "Kent State University", "King Abdullah University of Science and Technology", "Kyung Hee University", "Kyungpook National University", "La Trobe University", "Lanzhou University", "Lehigh University", "London School of Hygiene and Tropical Medicine", "Massey University", "Medical College of Wisconsin", "Medical University of Graz", "Medical University of Innsbruck", "Nagasaki University", "Nankai University", "National Central University", "National Sun Yat-Sen University", "National Yang Ming University", "Niigata University", "Osaka City University", "Peking Union Medical College", "Polytechnic University of Turin", "Pusan National University", "South China University of Technology", "Southeast University", "Southern Methodist University", "Stockholm School of Economics", "Technical University of Braunschweig", "Technical University of Lisbon", "Texas Tech University", "The Open University", "The University of Texas Medical Branch at Galveston", "The University of Tokushima", "Tianjin University", "Tongji University", "University of Alaska - Fairbanks", "University of Arkansas at Fayetteville", "University of Bayreuth", "University of Bielefeld", "University of Bremen", "University of Canterbury", "University of Chile", "University of Coimbra", "University of Duisburg-Essen", "University of Eastern Finland", "University of Essex", "University of Ferrara", "University of Graz", "University of Haifa", "University of Hannover", "University of Idaho", "University of Jena", "University of Jyvaskyla", "University of KwaZulu-Natal", "University of Ljubljana", "University of Malaya", "University of Maryland, Baltimore County", "University of Milan - Bicocca", "University of Nebraska Medical Center", "University of New Hampshire - Durham", "University of Palermo", "University of Pavia", "University of Quebec", "University of Rennes 1", "University of Roma - Tor Vergata", "University of Sherbrooke", "University of Surrey", "University of Szeged", "University of Technology, Sydney", "University of Tehran", "University of the Basque Country", "University of Tromso", "University of Wyoming", "University of Zagreb", "University of Zaragoza", "Utah State University", "Victoria University of Wellington", "Vienna University of Technology", "Wuhan University", "Xiamen University", "York University"]

relevant_roles = ["analyst", "analytics", "analysis", "data scientist", "scientist", "engineer", "developer", "software", "statistician", "data mining", "research", "consultant", "management", "modeling", "models", "engineering", "metrics", "optimization", "professional", "senior", "investment", "operations", "retail", "executives", "e-commerce", "staff", "securities", "principal", "supply chain", "data analytics", "analytics intern", "data analysis", "data analyst", "analyst intern", "lead team", "team lead", "science intern", "senior consultant", "senior analyst", "research assisstant", "financial consultant", "analytical consulting", "research consultant", "technical support", "business analyst", "project management", "associate", "director", "money managers", "data management", "leaders program", "cross-functional team", "vice president", "china analyst", "business intelligence", "principal investigator"]

statistics_skillz = ["sas", " r ", " r,", "time series", "linear regression", "machine learning", "data mining", "data science", "data mangement", "sql", "statistics", "modeling", "models", "data analysis", "decision trees", "classification", "regression analysis", "logistic regression", "spss", "tableau", "data visualization", "component analysis", "mathematics", "optimization", "financial", "quantitative", "probability", "stochastic", "regression", "economics", "decision support", "vector", "dimension", "linear algebra", "segmentation", "market basket", "customer segmentation", "statistical methods", "data warehousing", "google analytics"]

programming_languages = ["sas", "r", "visual basic", "vba", "python java", "python", "java", "c", "c++", "c#", "hadoop", "apache", "pig", "bash", "linux", "unix", "sql", "postgresql", "mysql", "nosql", "javascript", "ruby", "d3", "d3.js"]

certifications = ["certifications", "certified", "certification", "certificate", "base sas", "certificate program", "sigma certified", "leadership certificate", "deans certificate", "certificate deans", "financial certificate", "certified software", "segmentation certification", "certification sas", "certified base", "sas certified", "programmer sas", "base programmer", "developer certified", "certified associate", "certified yellow", "certificate machine", "certificate game", "certification business", "chemistry certificate"]

honors = ["honors awards", "economics award", "student award", "cum laude", "delta honors", "honors fraternity", "high honors", "honors awards", "honors: mathematics", "honors: departmental", "departmental honors;", "honors: phi", "international honor", "honor society", "honors academia", "honors", "honors work", "honors: dean's", "graduated honor", "engineering honors", "scholorship", "honors student", "departmental honors", "honors economics", "university honors", "honoree"]

awards = ["awarded us$ 4 million", "peer reviewed publication reputed journal", "pending patent applications", "cisco's spot award", "cisco's chief staff merit award", "bemis math science endowed scholarship", "reducing procurement costs 15% impacting profits", "brought process enhancements resulted in 25% man-hour efficiency", "neilson global operations leadership award 2013", "selection as top operations  associate", "peer nomination to deliver graduation speech", "awarded", "awarded advanced communicator bronze toastmaster", "awarded competent communicator", "awarded table topics champion", "award", "exceptional leadership service", "charles thomson senior design award", "silver award"]

# This converts a string to an array, removes some characters, and makes it lowercase
def resume_to_array(text):
  result = text
  result = result.replace(",","")
  result = result.replace("(","")
  result = result.replace(")","")
  result = result.replace("[","")
  result = result.replace("]","")
  result = result.replace("!","")
  result = result.lower()
  return result.split()

# This extracts the name of the applicant from the file name
# It doesn't work that well in general
# Works well for betas at least
def get_name(path_name):
  resume_file_name = path_name.lower().split('/')[-1]
  end_index = resume_file_name.index('resume')
  name = resume_file_name[0, end_index - 1]
  return name

# Compares mentions of a university with the dictionary
# Sets rank as the highest mentioned
# Emphasis on mentioned. Applicant may not actually have attended
def get_university_rank(text):
  rank = None
  temp_list = universities
  temp_list.reverse()
  for i, u in enumerate(temp_list):
    if text.find(u) >= 0:
      rank = 500 - i
  return rank

# Extracts the GPA
# Looks for format x.xx or x.x
# Some resumes list Grade instead of GPA
# Sets GPA as only the last one in the array (ie if multiple GPAs are present)
# This is finicky with extracting the correct number...
def get_gpa(text_list):
  resume_as_array = resume_to_array(text_list)
  gpa = None
  for i, r in enumerate(resume_as_array):
    if r.find('gpa') >= 0:
      gpa = re.match('[0-4][.][0-9][0-9]', r)
      if gpa == None:
        gpa = re.match('[0-4][.][0-9]', r)
        if gpa == None:
          gpa = re.match('[0-4][.][0-9][0-9]', resume_as_array[i + 1])
          if gpa == None:
            gpa = re.match('[0-4][.][0-9]', resume_as_array[i + 1])
          gpa = gpa.expand(resume_as_array[i + 1])
        else:
          gpa = gpa.expand(r)
  return gpa

# Checks to see if text includes these phrases
# Not very comprehensive in practice I think
def has_masters(text):
  result = 0
  if text.find('M.S.') >= 0 or text.find('M.A.') >= 0 or text.find('Master of Science') >= 0:
    result = 1
  return result

# Similar to masters, except with PhDs
def has_phd(text):
  result = 0
  if text.find('PhD') >= 0 or text.find('Ph.D') >= 0 or text.find('Doctor of Philosophy') >= 0:
    result = 1
  return result

# Checks to see if a relevant role is present
# This might be a counting stat instead
# Should check with Blackhawks
def has_relevant_role(text):
  result = 0
  for r in relevant_roles:
    if text.lower().find(r) >= 0:
      result += 1
  return result

# Counts the number of stats skillz, based on dictionary
def number_of_stats_skillz(text):
  result = 0
  for s in statistics_skillz:
    if text.lower().find(s) >= 0:
      result += 1
  return result

# Counts the number of programming languages, based on dictionary
def number_of_programming_languages(text_array):
  resume_as_array = resume_to_array(text_array)
  result = 0
  for p in programming_languages:
    if resume_as_array.count(p) > 0:
      result += 1
  return result

# Counts the number of certifications, based on dictionary
def number_of_certifications(text):
  result = 0
  for c in certifications:
    if text.lower().find(c) >= 0:
      result += 1
  return result

# Counts the number of honors, based on dictionary
def number_of_honors(text):
  result = 0
  for h in honors:
    if text.lower().find(h) >= 0:
      result += 1
  return result

# Counts the number of awards, based on dictionary
def number_of_awards(text):
  result = 0
  for a in awards:
    if text.lower().find(a) >= 0:
      result += 1
  return result

# Uses all those methods for a resume
# Returns a dictionary of all values
def compile_all(individual_resume_text):
  result = {}
  result["university_rank"] = get_university_rank(individual_resume_text)
  result["masters"] = has_masters(individual_resume_text)
  result["doctorate"] = has_phd(individual_resume_text)
  result["relevant_role"] = has_relevant_role(individual_resume_text)
  result["stats_skills"] = number_of_stats_skillz(individual_resume_text)
  result["certifications"] = number_of_certifications(individual_resume_text)
  result["honors"] = number_of_honors(individual_resume_text)
  result["awards"] = number_of_awards(individual_resume_text)
  result["gpa"] = get_gpa(individual_resume_text)
  result["programming_languages"] = number_of_programming_languages(individual_resume_text)
  return result

# Runs the compile_all method for all the resumes
for r in resumes_text:
  all_results.append(compile_all(r))

# Prints the dictionaries to the screen
print all_results

# Creates a new .txt file for the results
f = open("testfileutenn.txt", "w")
# Writes the header categories to the file. tab-delimited
f.write("university_rank\tmasters\tdoctorate\trelevant_role\tstats_skills\tcertifications\thonors\tawards\tgpa\tprogramming_languages\n")
# Loops through all resumes and writes them to the file
for r in all_results:
  # puts "#{key}: #{value}"
  f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (r["university_rank"], r["masters"], r["doctorate"], r["relevant_role"], r["stats_skills"], r["certifications"], r["honors"], r["awards"], r["gpa"], r["programming_languages"]))

f.close()

# Have a nice day