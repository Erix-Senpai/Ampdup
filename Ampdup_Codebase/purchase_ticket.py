from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import db, Event, Booking
from .forms import PurchaseForm
from datetime import datetime


purchase_ticket_bp = Blueprint('PurchaseTicket', __name__)

# Purchase ticket route
@purchase_ticket_bp.route('/<int:event_id>', methods=['POST'])
@login_required # Ensure user is logged in
def purchase_ticket(event_id):
    if not current_user.is_authenticated: #if user is not logged in, message is flashed
        flash('Please log in to purchase tickets')
        return redirect(url_for('auth.login'))  #Redirect to login if not authenticated

    #if user is logged in, proceed with ticket purchase
    else:
        event = db.session.get(Event, event_id) 
        if not event: #If event does not exist, message is flashed
            flash('Event not found.')
            return redirect(url_for('main.index'))
        
        purchaseform = PurchaseForm() #Create purchase form instance
        if purchaseform.validate_on_submit():
            ticket_quantity = int(request.form.get('quantity')) #getting the number of tickets from the form
             
        #create a new booking to store in the database
        new_order = Booking(
            user_id=current_user.id,
            event_id=event.id,
            quantity=ticket_quantity,
            order_date= datetime.today()
        )

        # Deduct the purchased tickets from the remaining tickets
        event.ticket_remain = event.ticket_remain - ticket_quantity
        db.session.add(new_order) 
        db.session.commit()
        #flash successful purchase message to user with the order ID
        flash(f" Order ID: {new_order.id} \nSuccessfully purchased {ticket_quantity} ticket(s) for {event.title}!") 
        return redirect(url_for('BookingHistory.Get_Booking')) #redirect user to their booking history



 