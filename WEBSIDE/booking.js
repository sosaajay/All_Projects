// JAVASCRIPT FOR BOOKING FUNCTIONALITY
document.addEventListener('DOMContentLoaded', function() {
    // Set minimum date to today
    const dateInput = document.getElementById('date');
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);

    // Form Submission Handler
    document.getElementById('bookingForm').addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form values
        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;
        const guests = document.getElementById('guests').value;
        const requests = document.getElementById('requests').value;

        // Validate form
        if (!name || !phone || !email || !date || !time || !guests) {
            alert('Please fill in all required fields.');
            return;
        }

        // Generate booking reference
        const bookingRef = 'RS' + Date.now().toString().slice(-6);

        // Show success modal
        document.getElementById('bookingRef').textContent = bookingRef;
        document.getElementById('bookingDate').textContent = date;
        document.getElementById('bookingTime').textContent = time;
        document.getElementById('bookingGuests').textContent = guests + ' Guest(s)';
        document.getElementById('bookingModal').style.display = 'flex';

        // Log booking data (In real app, send to server)
        console.log('Booking Details:', {
            name, phone, email, date, time, guests, requests, bookingRef
        });

        // Reset form
        this.reset();
    });

    // Close Modal Function
    function closeModal() {
        document.getElementById('bookingModal').style.display = 'none';
    }

    // Close modal when clicking outside
    document.getElementById('bookingModal').addEventListener('click', function(e) {
        if (e.target === this) {
            closeModal();
        }
    });
});