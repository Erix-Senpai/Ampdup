from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import db, Event, Booking
from .forms import PurchaseForm
from datetime import datetime


purchase_ticket_bp = Blueprint('PurchaseTicket', __name__)


@purchase_ticket_bp.route('/<int:event_id>', methods=['POST'])
@login_required
def purchase_ticket(event_id):
    if not current_user.is_authenticated:
        flash('Please log in to purchase tickets')
        return redirect(url_for('auth.login'))  

    else:
        event = db.session.get(Event, event_id)
        if not event:
            flash('Event not found.')
            return redirect(url_for('main.index'))
        
        purchaseform = PurchaseForm()
        if purchaseform.validate_on_submit():
            ticket_quantity = int(request.form.get('quantity'))
             

        new_order = Booking(
            user_id=current_user.id,
            event_id=event.id,
            quantity=ticket_quantity,
            order_date= datetime.today()

        )
        event.ticket_remain = event.ticket_remain - ticket_quantity
        db.session.add(new_order)
        db.session.commit()
        flash(f" Order ID: {new_order.id} \nSuccessfully purchased {ticket_quantity} ticket(s) for {event.title}!")
        return redirect(url_for('BookingHistory.Get_Booking'))



 