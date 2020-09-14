// Syed Yasoob Ali 
// 500953533

import java.util.ArrayList;

// Make class Student implement the Comparable interface
// Two student objects should be compared by their name
public class Student
{
  private String name;
  private String id;
  public  ArrayList<CreditCourse> courses;
  
  //Student constructor
  public Student(String name, String id)
  {
	 this.name = name;
	 this.id   = id;
	 courses   = new ArrayList<CreditCourse>();
  }
  
  //Returns student ID
  public String getId()
  {
	  return id;
  }
  
  //Returns student name
  public String getName()
  {
	  return name;
  }
  
  // add a credit course to list of courses for this student
  
  //Adds a course to the student's course array list and sets it to an active course
  public void addCourse(String courseName, String courseCode, String descr, String format,String sem, double grade)
  {
	  // create a CreditCourse object
	  // set course active
	  // add to courses array list
	  
	  CreditCourse newCourse = new CreditCourse(courseName, courseCode, descr, format, sem, grade);
	  newCourse.setActive();
	  courses.add(newCourse);
	  
  }
  
  
  
  // Prints a student transcript
  // Prints all completed (i.e. non active) courses for this student (course code, course name, 
  // semester, letter grade
  // see class CreditCourse for useful methods
  
  //Cycles through all courses that the student is enrolled in and prints them
  public void printTranscript()
  {
	  for (int i = 0; i < courses.size(); i++)
	  {
			//Will only print courses that are finished, so checks to see if the course is active first
			if(courses.get(i).getActive() == false)
			{
				System.out.println(courses.get(i));
			}
	  }
  }
  
  // Prints all active courses this student is enrolled in
  // see variable active in class CreditCourse
  
  //Cycles through all courses that student is enrolled in and prints only active ones
  public void printActiveCourses()
  {
	 for (int j = 0; j < courses.size(); j++)
	 {
		 //Checks to see if course is active before printing
		 if(courses.get(i).getActive() == true)
		 {
			 System.out.println(courses.get(i));
		 }
	 }
  }
  
  // Drop a course (given by courseCode)
  // Find the credit course in courses arraylist above and remove it
  // only remove it if it is an active course
  
  //Takes in a courseCode as parameter and cycles through all courses to remove one matching that code
  public void removeActiveCourse(String courseCode)
  {
	 for (int k = 0; k < courses.size(); k++)
	 {
		 if(courses.get(k).getCode().equals(courseCode))
		 {
			 courses.remove(courses.get(k));
		 }
	 }
  }
  
  //Returns name and ID of student
  public String toString()
  {
	  return "Student ID: " + id + " Name: " + name;
  }
  
  // override equals method inherited from superclass Object
  // if student names are equal *and* student ids are equal (of "this" student
  // and "other" student) then return true
  // otherwise return false
  // Hint: you will need to cast other parameter to a local Student reference variable
  
  //Compares other object(which is turned into a student object) with the student to see if the IDs and names match
  public boolean equals(Object other)
  {
	  //First compares name with student and other and then ID
	  if (this.getName().equalsIgnoreCase(((Student) other).getName()))
	  {
		  if (this.getId().equalsIgnoreCase(((Student) other).getId()))
		  {
			  return true;
		  }
	  }
	  //otherwise, return false
	  return false;
  }
  
}
