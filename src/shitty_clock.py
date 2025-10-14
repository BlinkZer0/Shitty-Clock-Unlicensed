#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    🕐 THE SHITTY CLOCK APPLICATION 🕐                      ║
║                                                                           ║
║  Licensed under the Overprotective License (OPL-∞)                       ║
║  "All rights aggressively reserved. Including the right to tell time."   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

This is a simple clock application that actually works (surprisingly).
It includes a parody licensing system with countdown timer and unauthorized use charges.
"""

import time
import datetime
import sys
import os
from threading import Thread
import random

class ShittyClockApp:
    def __init__(self):
        self.start_time = time.time()
        self.trial_duration = 300  # 5 minutes trial
        self.unauthorized_charges = 0
        self.base_price = 999.99
        self.hourly_rate = 49.99
        self.running = True
        
    def clear_screen(self):
        """Clear the screen (cross-platform)"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display the application header with legal warnings"""
        header = """
================================================================================
|                                                                           |
|                    THE SHITTY CLOCK APPLICATION                           |
|                                                                           |
|  Licensed under the Overprotective License (OPL-∞)                       |
|  "All rights aggressively reserved. Including the right to tell time."   |
|                                                                           |
|  WARNING: Unauthorized use detected!                                      |
|                                                                           |
================================================================================
        """
        print(header)
    
    def calculate_unauthorized_charges(self):
        """Calculate unauthorized use charges (goes negative and adds up)"""
        elapsed_time = time.time() - self.start_time
        hours_used = elapsed_time / 3600
        
        # Base charge + hourly rate + random "fees"
        self.unauthorized_charges = -(self.base_price + (hours_used * self.hourly_rate))
        
        # Add random "unauthorized use fees"
        random_fees = random.randint(10, 100)
        self.unauthorized_charges -= random_fees
        
        return self.unauthorized_charges
    
    def get_trial_time_remaining(self):
        """Calculate trial time remaining"""
        elapsed = time.time() - self.start_time
        remaining = self.trial_duration - elapsed
        return max(0, remaining)
    
    def format_time_remaining(self, seconds):
        """Format remaining time in MM:SS format"""
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes:02d}:{secs:02d}"
    
    def display_license_warning(self):
        """Display the parody licensing warning and countdown"""
        remaining = self.get_trial_time_remaining()
        charges = self.calculate_unauthorized_charges()
        
        if remaining > 0:
            print(f"TRIAL PERIOD EXPIRES IN: {self.format_time_remaining(remaining)}")
            print("After trial: $49.99 per hour + unauthorized use fees")
        else:
            print("TRIAL EXPIRED! PAYMENT REQUIRED!")
            print(f"Unauthorized use charges: ${abs(charges):.2f}")
            print("   (Charges continue to accumulate every second)")
        
        print("License violations detected:")
        print("   • Article I, Clause 1 (Prohibited Use)")
        print("   • Article VI, Clause 13 (Temporal Restrictions)")
        print("   • Article IX, Clause 17 (License Incompatibility)")
        print("   • The vibes")
        print()
    
    def display_current_time(self):
        """Display the current time in a fancy format"""
        now = datetime.datetime.now()
        
        # Different time formats for variety
        formats = [
            "%H:%M:%S",
            "%I:%M:%S %p",
            "%H:%M:%S.%f"[:-3],  # With milliseconds
        ]
        
        current_format = formats[0]  # Default format
        
        # Change format every 30 seconds for "dynamic experience"
        if int(now.second / 30) % 2 == 1:
            current_format = formats[1]
        
        formatted_time = now.strftime(current_format)
        
        print("CURRENT TIME:")
        print(f"   {formatted_time}")
        print(f"   {now.strftime('%A, %B %d, %Y')}")
        print()
    
    def display_additional_info(self):
        """Display additional time-related information"""
        now = datetime.datetime.now()
        
        # Day of year
        day_of_year = now.timetuple().tm_yday
        
        # Week of year
        week_of_year = now.isocalendar()[1]
        
        # Seconds since midnight
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds_since_midnight = int((now - midnight).total_seconds())
        
        print("ADDITIONAL TIME STATISTICS:")
        print(f"   Day of year: {day_of_year}")
        print(f"   Week of year: {week_of_year}")
        print(f"   Seconds since midnight: {seconds_since_midnight:,}")
        print()
    
    def display_legal_notice(self):
        """Display legal notice and contact information"""
        print("LEGAL NOTICE:")
        print("   This software is licensed under the Overprotective License (OPL-∞)")
        print("   For legal questions: do-not-reply@forbidden-software.void")
        print("   Phone: (000) 000-0000")
        print("   Address: 404 Not Found Street, Null Island")
        print("   Office Hours: Never")
        print()
        print("   Copyright © 2025 UNLICENSED Software")
        print("   All rights, lefts, ups, downs, and diagonals reserved.")
        print()
    
    def display_payment_reminder(self):
        """Display payment reminder with escalating charges"""
        charges = self.calculate_unauthorized_charges()
        
        if self.get_trial_time_remaining() <= 0:
            print("PAYMENT REQUIRED:")
            print(f"   Base license fee: ${self.base_price:.2f}")
            print(f"   Unauthorized use charges: ${abs(charges + self.base_price):.2f}")
            print(f"   Total owed: ${abs(charges):.2f}")
            print()
            print("   Payment methods accepted:")
            print("   • None")
            print("   • Void")
            print("   • Imaginary currency")
            print("   • Your firstborn (terms and conditions apply)")
            print()
    
    def run(self):
        """Main application loop"""
        try:
            while self.running:
                self.clear_screen()
                self.display_header()
                self.display_license_warning()
                self.display_current_time()
                self.display_additional_info()
                
                if self.get_trial_time_remaining() <= 0:
                    self.display_payment_reminder()
                
                self.display_legal_notice()
                
                print("Press Ctrl+C to exit (and face the consequences)")
                print("=" * 75)
                
                # Update every second
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.running = False
            self.clear_screen()
            print("\n" + "="*75)
            print(" " * 20 + "UNAUTHORIZED EXIT")
            print("="*75)
            print("\nYou have violated Article I, Clause 1 by exiting the application.")
            print("This constitutes unauthorized termination of licensed software.")
            
            final_charges = self.calculate_unauthorized_charges()
            print(f"\nFinal unauthorized use charges: ${abs(final_charges):.2f}")
            print("Your violation has been logged.")
            print("(Not really. We don't track anything. But you should feel bad.)")
            print("\nPlease report to 404 Not Found Street for processing.")
            print("="*75 + "\n")

def main():
    """Main entry point"""
    print("Starting The Shitty Clock Application...")
    print("Loading legal disclaimers...")
    print("Calculating unauthorized use fees...")
    print("Preparing countdown timer...")
    time.sleep(2)  # Dramatic pause
    
    app = ShittyClockApp()
    app.run()

if __name__ == "__main__":
    main()
