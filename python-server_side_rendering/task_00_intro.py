import os
import sys

def generate_invitations(template, attendees):
    """
    Template ve katılımcı listesinden kişiselleştirilmiş davetiye dosyaları oluşturur
    
    Parameters:
    template (str): Davetiye şablonu metni
    attendees (list): Katılımcı bilgilerini içeren dictionary listesi
    
    Returns:
    None
    """
    
    # ========== INPUT VALIDATION ==========
    
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.", file=sys.stderr)
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.", file=sys.stderr)
        return
    
    # Check if each attendee is a dictionary
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i} is not a dictionary.", file=sys.stderr)
            return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.", file=sys.stderr)
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.", file=sys.stderr)
        return
    
    # ========== PROCESS EACH ATTENDEE ==========
    
    files_created = 0
    
    for i, attendee in enumerate(attendees, start=1):
        try:
            # Start with the template
            personalized_template = template
            
            # Define placeholders and their default values
            placeholders = {
                '{name}': 'N/A',
                '{event_title}': 'N/A', 
                '{event_date}': 'N/A',
                '{event_location}': 'N/A'
            }
            
            # Replace each placeholder with attendee data or default
            for placeholder, default_value in placeholders.items():
                # Get the key name from placeholder (remove {})
                key = placeholder.strip('{}')
                
                # Get value from attendee or use default
                value = attendee.get(key)
                
                # Handle None values
                if value is None:
                    value = default_value
                elif isinstance(value, str) and not value.strip():
                    value = default_value
                
                # Replace the placeholder in the template
                personalized_template = personalized_template.replace(placeholder, str(value))
            
            # Create output filename
            output_filename = f"output_{i}.txt"
            
            # Write to file
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(personalized_template)
            
            print(f"Created: {output_filename}")
            files_created += 1
            
        except Exception as e:
            print(f"Error processing attendee {i}: {str(e)}", file=sys.stderr)
    
    # ========== FINAL SUMMARY ==========
    
    if files_created > 0:
        print(f"\nSuccessfully created {files_created} invitation file(s).")
    else:
        print("No invitation files were created.", file=sys.stderr)
