import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "workout_log.txt")
SUMMARY_PATH = os.path.join(BASE_DIR, "fitness_summary.txt")
ERROR_LOG_PATH = os.path.join(BASE_DIR, "errors.log")

class LogError(Exception):
    pass


# ---------------------------------------------------------------------------
# Step 1: File Handling -- read the journal
# ---------------------------------------------------------------------------
def read_entries(path):
    
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        return lines

def parse_entry(line):
    
    line  = line.strip()
    
    date_match = re.search(r"\b\d{4}-\d{2}-\d{2}\b", line)
    
    if not date_match:
        raise LogError("Missing Date")
    
    date = date_match.group()
    
    
    exercise_match = re.search(r"\|\s*([A-Za-z][A-Za-z ]*?)\s*\|", line)
     
    if not exercise_match:
        raise LogError("Missing exercise name")
    
    exercise = exercise_match.group(1).strip()
    
    if not exercise:
        raise LogError("Missing excercise name")
    
    duration_match = re.search(r"(-?\d+(?:\.\d+)?)\s*min(?:ute)?s?\b", line, re.IGNORECASE)
    
    if not duration_match:
        raise LogError("Missing or invalid duration")
    
    duration = float(duration_match.group(1))
    
    if duration <= 0:
        raise LogError("Duration must be greater than zero ")
    
    if duration.is_integer():
        duration = int(duration)
        
    distance_match = re.search(r"(\d+(?:\.\d+)?)\s*km\b", line, re.IGNORECASE)
    
    if distance_match:
        distance_km = float(distance_match.group(1))
    else:
        distance_km =  None
        
    reps_match = re.search(r"(\d+)\s*reps?\b", line, re.IGNORECASE)
    
    if reps_match:
        reps =int(reps_match.group(1))
    else:
        reps = None
    

    
    return {
        "date": date,
        "exercise": exercise,
        "duration_minutes": duration,
        "distance_km": distance_km,   # or None
        "reps": reps,         # or an int
        
        }

def summarise(entries):
     
     total_minutes = 0
     total_distance_km = 0.0
     sessions_per_exercise = {}
     longest_session = None       # the entry dict with the most minutes
     
     for entry in entries:
         
        total_minutes += entry["duration_minutes"]
         
        if entry["distance_km"] is not None:
            total_distance_km += entry["distance_km"]
             
        exercise = entry["exercise"]
        
        if exercise in sessions_per_exercise:
            sessions_per_exercise[exercise] += 1
        else:
            sessions_per_exercise[exercise] = 1
            
        if longest_session is None:
            longest_session =  entry
        elif entry["duration_minutes"] > longest_session["duration_minutes"]:
            longest_session = entry

     return {
         
            "total_minutes": total_minutes,
            "total_distance_km": total_distance_km,
            "sessions_per_exercise": sessions_per_exercise,
            "longest_session": longest_session,
            
         }


def process_log(input_path, summary_path, error_log_path):
        
        lines = read_entries(input_path)
        
        good_entries = []
        bad_entries = []
        processed_count = 0
        
        for line in lines:
            
            try:
                entry = parse_entry(line)
            except LogError as error:
                bad_entries.append((line.strip(), str(error)))
                
            else:
                good_entries.append(entry)
                
            finally:
                processed_count += 1
                
        summary = summarise(good_entries)
        
        with open(summary_path, "w", encoding="utf-8") as f:
            
            f.write("========== FITNESS SUMMARY ==========\n\n")
            
            f.write(f"Total workout minutes: {summary['total_minutes']}\n")
            
            f.write(f"Total distance: {summary['total_distance_km']}km\n")
            
            f.write("\nSessions per exercise:\n")
            
            if summary["sessions_per_exercise"]:
                for exercise, count in summary["sessions_per_exercise"].items():
                    f.write(f"- {exercise}: {count} session(s)\n")
                    
            else:
                f.write("No valid workout sessions found.\n")
                
            f.write("\nLongest session:\n")
                
            if summary["longest_session"] is not None:
                longest = summary["longest_session"]
                    
                f.write(f"Date: {longest['date']}\n")
                f.write(f"Exercise: {longest['exercise']}\n")
                f.write(f"Duration: {longest['duration_minutes']}minutes\n")
                    
            else:
                f.write("No valid workout sessions found.\n")
                    
            f.write("\n")
            f.write(f"Valid entries: {len(good_entries)}\n")
            f.write(f"Invalid entries: {len(bad_entries)}\n")
            f.write(f"Total lines processed: {processed_count}\n")

        with open(error_log_path, "w", encoding="utf-8") as f:

            if not bad_entries:
                f.write("No errors found. All lines were valid.\n")

            else:
                for bad_line, reason in bad_entries:
                    f.write(f"Invalid line: {bad_line}\n")
                    f.write(f"Reason: {reason}\n")
                    f.write("\n")


        return summary

def main():
    
    print("Fitness Tracker Log Analyzer")
    print("Reading journal:", INPUT_PATH)
    print()
    
    try:
         summary= process_log(
            INPUT_PATH,
            SUMMARY_PATH,
            ERROR_LOG_PATH
        )
         
    except FileNotFoundError:
        print("Error: workout_log.txt could not be found.")
        print("Make sure it is in the same folder as starter.py.")
        return

    except OSError as error:
        print("A file error occurred:", error)
        return

    print("========== RESULTS ==========")

    print("Total minutes exercised:", summary.get("total_minutes", 0))
    
    print("Total distance:", f"{summary['total_distance_km']}km")
    
    longest = summary["longest_session"]
    
    if longest is not None:
        print(f"Longest session: {longest['exercise']} - {longest['duration_minutes']} minutes")
    else: 
        print("Longest session: None")
        
    print()
    print("Summary written to:", SUMMARY_PATH)
    print("Errors written to :", ERROR_LOG_PATH)

if __name__ == "__main__":
    main()
