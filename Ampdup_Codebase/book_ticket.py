from flask import Blueprint, flash, render_template, request, url_for, redirect
book_ticket_bp = Blueprint('book_ticket', __name__)

@book_ticket_bp.route('/book_ticket', methods=['POST'])
def Ticket():
    return redirect(url_for('BookingHistory.Get_Booking'))
