import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem


def main():
    app = QApplication(sys.argv)

    # Create a QTableWidget
    table = QTableWidget()
    table.setColumnCount(3)
    table.setRowCount(5)

    # Fill the table with some dummy data
    for row in range(5):
        for col in range(3):
            table.setItem(row, col, QTableWidgetItem("Row {}, Col {}".format(row + 1, col + 1)))

    # Get the horizontal and vertical header objects
    horizontal_header = table.horizontalHeader()
    vertical_header = table.verticalHeader()

    # Print the size of each header row
    for row in range(table.rowCount()):
        print("Vertical Header Row {}: {}".format(row, vertical_header.sectionSize(row)))

    # Print the size of each header column
    for col in range(table.columnCount()):
        print("Horizontal Header Column {}: {}".format(col, horizontal_header.sectionSize(col)))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
