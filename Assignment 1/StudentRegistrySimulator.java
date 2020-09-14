// Syed Yasoob Ali
// 500953533

import java.util.ArrayList;
import java.util.Scanner;

public class StudentRegistrySimulator 
{
  public static void main(String[] args)
  {
	  Registry registry = new Registry();
	  
	  Scanner scanner = new Scanner(System.in);
	  System.out.print(">");
	  
	  while (scanner.hasNextLine())
	  {
		  String inputLine = scanner.nextLine();
		  if (inputLine == null || inputLine.equals("")) continue;
		  
		  Scanner commandLine = new Scanner(inputLine);
		  String command = commandLine.next();
		  
		  if (command == null || command.equals("")) continue;
		  
		  else if (command.equalsIgnoreCase("L") || command.equalsIgnoreCase("LIST"))
		  {
			  registry.printAllStudents();
		  }
		  else if (command.equalsIgnoreCase("Q") || command.equalsIgnoreCase("QUIT"))
			  return;
		  
		  else if (command.equalsIgnoreCase("REG"))
		  {
			  // register a new student in registry
			  // get name and student id string 
			  // e.g. reg JohnBoy 74345
			  // Checks:
			  //  ensure name is all alphabetic characters
			  //  ensure id string is all numeric characters
			  
			  String name = commandLine.next();
			  String id = commandLine.next();
			  
			  if (isStringOnlyAlphabet(name))
			  {
				  if (isNumeric(id))
				  {
					  registry.addNewStudent(name,id);
				  }
			  }
			  
		  }
		  else if (command.equalsIgnoreCase("DEL"))
		  {
			  // delete a student from registry
			  // get student id
			  // ensure numeric
			  // remove student from registry
			  
			  String id = commandLine.next();
			  
			  if (isNumeric(id))
			  {
				  registry.removeStudent(id);
			  }
			  
		  }
		  
		  else if (command.equalsIgnoreCase("ADDC"))
		  {
			 // add a student to an active course
			 // get student id and course code strings
			 // add student to course (see class Registry)
			 
			 String id = commandLine.next();
			 String courseCode = commandLine.next();
			 
			 registry.addCourse(id, courseCode);
		
			  
		  }
		  else if (command.equalsIgnoreCase("DROPC"))
		  {
			  // get student id and course code strings
			  // drop student from course (see class Registry)
			  
			  string id = commandLine.next();
			  string courseCode = commandLine.next();
			  
			  registry.dropCourse(id, courseCode);
			  
		  }
		  else if (command.equalsIgnoreCase("PAC"))
		  {
			  // print all active courses
			  
			  registry.printActiveCourses();
			  
		  }		  
		  else if (command.equalsIgnoreCase("PCL"))
		  {
			  // get course code string
			  // print class list (i.e. students) for this course
			  
			  string courseCode = commandLine.next();
			  
			  registry.printClassList(courseCode);
			  
			  
		  }
		  else if (command.equalsIgnoreCase("PGR"))
		  {
			  // get course code string
			  // print name, id and grade of all students in active course
			  
			  string courseCode = commandLine.next();
			  
			  ActiveCourse newActiveCourse = new ActiveCourse(courseCode);
			  newActiveCourse.printGrades();
			  
			  
		  }
		  else if (command.equalsIgnoreCase("PSC"))
		  {
			  // get student id string
			  // print all credit courses of student
			  
			  string id = commandLine.next();
			  
			  // idk yet
			  
		  }
		  else if (command.equalsIgnoreCase("PST"))
		  {
			  // get student id string
			  // print student transcript
			  
			  string id = commandLine.next();
			  
			  //Student.printTranscript();
			  
		  }
		  else if (command.equalsIgnoreCase("SFG"))
		  {
			  // set final grade of student
			  // get course code, student id, numeric grade
			  // use registry to set final grade of this student (see class Registry)
		  }
		  else if (command.equalsIgnoreCase("SCN"))
		  {
			  // get course code
			  // sort list of students in course by name (i.e. alphabetically)
			  // see class Registry
			  
		  }
		  else if (command.equalsIgnoreCase("SCI"))
		  {
			// get course code
			// sort list of students in course by student id
			// see class Registry
		  }
		  System.out.print("\n>");
	  }
  }
  
  
  //Takes in a string and checks to see if it contains only alphabetic, will return true if true 
  private static boolean isStringOnlyAlphabet(String str) 
  { 
      // write method to check if string str contains only alphabetic characters 
	  
	  // First, convert the string to all lower case in order to compare easily
	  // And then create an array out of all the characters
	  str = str.toLowerCase();
	  char[] characterArray = str.toCharArray();
	  
	  //Cycles through each character and checks to see if it is within the range of 'a' to 'z'
	  //If it is not, then the method will return False, otherwise, it will return True
	  for (int j = 0; j < characterArray.length; j++)
	  {
		  if (!(characterArray[i] >= 'a' && characterArray[i] <= 'z'))
		  {
			  return false;
		  }
	  }
	  
	  return true;
  } 
  
  //Takes in a string and checks to see if it contains only numbers, will return true if true
  public static boolean isNumeric(String str)
  {
      // write method to check if string str contains only numeric characters
	  
	  //Checks string to see if it contains 0 through 9. If so, return true, otherwise, return false.
	  if (str.matches("[0-9]+"))
	  {
		  return true;
	  }
	  
	  return false;
  }
  
  
}