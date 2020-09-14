// Syed Yasoob Ali
// 500953533

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

// Active University Course
 
 // ActiveCourse is an extension of Course.java
public class ActiveCourse extends Course
{
	private ArrayList<Student> students; 
	private String             semester;
	
	   
   // Add a constructor method with appropriate parameters
   // should call super class constructor to initialize inherited variables
   // make sure to *copy* students array list being passed in into new arraylist of students
   // see class Registry to see how an ActiveCourse object is created and used
   
   //Constructor takes in parameters listed below, most of them coming from the Course class
   public ActiveCourse(String name, String code, String descr, String fmt,String semester,ArrayList<Student> students)
   {
	   super(name,code,descr,fmt);
	   this.semester = semester;
	   this.students = students;
   }
   
   //Returns the semester that course is currently being taken in
   public String getSemester()
   {
	   return semester;
   }
   
   // Prints the students in this course  (name and student id)
   public void printClassList()
   {
	   for (int i = 0; i < students.size(); i++)
	   {
		   System.out.println(students.get(i).getName() + " " + students.get(i).getId());
	   }
   }
   
   // Prints the grade of each student in this course (along with name and student id)
   public void printGrades()
   {
	   for (int j = 0; j < students.size(); j++)
	   {
		   System.out.println(students.get(j).getName() + " " + students.get(j).getId() + " " + students.get(j).getGrade());
	   }
   }
   
   // Returns the numeric grade in this course for this student
   // If student not found in course, return 0 
   public double getGrade(String studentId)
   {
	  // Search the student's list of credit courses to find the course code that matches this active course
	  // see class Student method getGrade() 
	  // return the grade stored in the credit course object
	  for (int i = 0; i < students.size(); i++)
	  {
		  if (students.courses.get(i).equals(studentId))
		  {
			  for (int j = 0; j < courses.size(j); j++)
			  {
					return (students.courses.get(i).grade);
		      }
		  }
		  
	  }
	  
	  
	  
	  return 0; 
   }
   
   // Returns a String containing the course information as well as the semester and the number of students 
   // enrolled in the course
   // must override method in the superclass Course and use super class method getDescription()
   
   //Returns the course description as well as the semester and course size
   public String getDescription()
   {
	   return super.getDescription() + " " + this.semester + " " + students.size();
   }
    
   
   // Sort the students in the course by name using the Collections.sort() method with appropriate arguments
   // Make use of a private Comparator class below
   
   //Uses collections method to create a comparator for names
   public void sortByName()
   {
 	  Collections.sort(students, new NameComparator());
   }
   
   // Fill in the class so that this class implement the Comparator interface
   // This class is used to compare two Student objects based on student name
   
   //Implements the comparator method for student and compares 2 student names
   private class NameComparator implements Comparator<Student>
   {
		public int compare(Student a, Student b)
		{
			return(a.getName().compareTo(b.getName()));
		}
   }
   
   // Sort the students in the course by student id using the Collections.sort() method with appropriate arguments
   // Make use of a private Comparator class below
   
   //Uses collections method to create a comparator for IDs
   public void sortById()
   {
 	  Collections.sort(students, new IdComparator());
   }
   
   // Fill in the class so that this class implement the Comparator interface
   // This class is used to compare two Student objects based on student id
   
   //Implements the comparator method for student and compares 2 student IDs
   private class IdComparator implements Comparator<Student>
   {
		public int compare(Student a, Student b)
		{
			return(a.getId().compareToIgnoreCase(b.getId()));
		}
   }
}
