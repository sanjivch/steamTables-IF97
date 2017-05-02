#ifndef STEAMTABLE_H
#define STEAMTABLE_H

#include <QMainWindow>

namespace Ui {
class steamTable;
}

class steamTable : public QMainWindow
{
    Q_OBJECT

public:
    explicit steamTable(QWidget *parent = 0);
    ~steamTable();



private slots:
    void on_calcButton_clicked();

    void on_SIButton_clicked();

    void on_MKSButton_clicked();

    void on_EnglishButton_clicked();

    void on_resetButton_clicked();

private:
    Ui::steamTable *ui;
};

#endif // STEAMTABLE_H
